from pyspark.sql.functions import pandas_udf, PandasUDFType
from cerebralcortex.core.datatypes import DataStream
from cerebralcortex.core.metadata_manager.stream.metadata import Metadata, DataDescriptor, \
    ModuleMetadata
import pandas as pd
from cerebralcortex import Kernel
from pyspark.sql import functions as F
import numpy as np
CC = Kernel("/home/jupyter/cc3_conf/", study_name='mperf')

def get_metadata1(data,
                  wrist,
                  sensor_name='motionsensehrvmperf',
                  ppg_columns=('red','infrared','green'),
                  acl_columns=('aclx','acly','aclz')):
    """
    :param data: input stream
    :param wrist: which wrist the data was collected from
    :param sensor_name: name of sensor
    :param ppg_columns: columns in the input dataframe referring to multiple ppg channels
    :param acl_columns: columns in the input dataframe referring to accelerometer channels

    :return: metadata of output stream
    """
    stream_name = "org.md2k."+str(sensor_name)+"."+str(wrist)+".wrist.bandpass.filtered.acl.filtered"
    stream_metadata = Metadata()
    stream_metadata.set_name(stream_name).set_description("Bandpass Filtered PPG data") \
        .add_dataDescriptor(DataDescriptor().set_name("timestamp").set_type("datetime")) \
        .add_dataDescriptor(DataDescriptor().set_name("localtime").set_type("datetime")) \
        .add_dataDescriptor(DataDescriptor().set_name("version").set_type("int")) \
        .add_dataDescriptor(DataDescriptor().set_name("user").set_type("string"))

    for c in ppg_columns:
        stream_metadata.add_dataDescriptor(DataDescriptor().set_name(c).set_type("double").set_attribute("description",
                                                                                                         "ppg channel "+c))
    for c in acl_columns:
        stream_metadata.add_dataDescriptor(DataDescriptor().set_name(c).set_type("double").set_attribute("description",
                                                                                                         "accelerometer channel "+c))

    stream_metadata.add_module(
        ModuleMetadata().set_name("ppg").set_attribute("url", "http://md2k.org/").set_author(
            "Md Azim Ullah", "mullah@memphis.edu"))
    return stream_metadata


def filter_60sec_data(data,
                      wrist,
                      Fs = 25,
                      acceptable = .8,
                      window_duration = 60):
    schema = data.schema
    @pandas_udf(schema, PandasUDFType.GROUPED_MAP)
    def acl_variance_filter(df):
        if df.shape[0]<Fs*acceptable*window_duration:
            return pd.DataFrame([],columns=df.columns)
        df = df.sort_values('timestamp').reset_index(drop=True)
        #         df['mag'] = df.apply(lambda a:np.sqrt(a['aclx']**2+a['acly']**2+a['aclz']**2),axis=1)
        variance = np.sqrt(df['aclx'].std()**2+df['acly'].std()**2+df['aclz'].std()**2)
        #         df.drop(columns=['mag'],inplace=True)
        if variance<.21:
            return pd.DataFrame([],columns=df.columns)
        else:
            print('-'*40,'This works')
            return df
    win = F.window("timestamp", windowDuration='60 seconds', startTime='0 seconds')
    ppg_filtered = data._data.groupBy(['user','version']+[win]).apply(acl_variance_filter)
    metadata1 = get_metadata1(data,wrist=wrist)
    ds = DataStream(data=ppg_filtered,metadata=metadata1)
    return ds


wrist = 'left'
data = CC.get_stream('org.md2k.motionsensehrvmperf.left.'+str(wrist)+'.bandpass.filtered')
ds = filter_60sec_data(data,wrist=wrist)
CC.save_stream(ds)