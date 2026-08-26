# st.py
# Link: /store/user/ksavva/data/HLepRare/skim_2024_v2/Run3_2022

import cmsdb.processes as procs
from cmsdb.campaigns.run2_2018_taupol_nano_v15 import campaign_run2_2018_taupol_nano_v15 as cpn



cpn.add_dataset(
    name='st_tchannel_t_powheg',
    id=18150110,
    is_data=False,
    processes=[procs.st_tchannel_t],
    keys=['/ST_t-channel_top_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM'],
    n_files=169,
    n_events=2737505.0, # this n_events is the gensumwt
    aux={'n_events': 2973675} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='st_tchannel_tbar_powheg',
    id=18150111,
    is_data=False,
    processes=[procs.st_tchannel_tbar],
    keys=['/ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM'],
    n_files=101,
    n_events=1325389.0, # this n_events is the gensumwt
    aux={'n_events': 1433215} # n_events in aux is the nEvents produced
)


cpn.add_dataset(
    name='st_tw_t_powheg',
    id=18150121,
    is_data=False,
    processes=[procs.st_twchannel_t],
    keys=['/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM'],
    n_files=15,
    n_events=9643983.0, # this n_events is the gensumwt
    aux={'n_events': 9644321} # n_events in aux is the nEvents produced
)


cpn.add_dataset(
    name='st_tw_tbar_powheg',
    id=18150131,
    is_data=False,
    processes=[procs.st_twchannel_tbar],
    keys=['/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM'],
    n_files=12,
    n_events=9182711.0, # this n_events is the gensumwt
    aux={'n_events': 9183029} # n_events in aux is the nEvents produced
)
