# wj.py
# Link: /store/user/ksavva/data/HLepRare/skim_2024_v2/Run3_2022
# ID: 181503XX

import cmsdb.processes as procs
from cmsdb.campaigns.run2_2018_taupol_nano_v15 import campaign_run2_2018_taupol_nano_v15 as cpn


# NLO
cpn.add_dataset(
    name='wj_incl_amcatnlo',
    id=18150301,
    is_data=False,
    processes=[procs.w_lnu],
    keys=['/WJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM'],
    n_files=28,
    n_events=183585526.0, # this n_events is the gensumwt
    aux={'n_events': 183585526} # n_events in aux is the nEvents produced
)
cpn.add_dataset(
    name='wj_0j_amcatnlo',
    id=18150302,
    is_data=False,
    processes=[procs.w_lnu_0j],
    keys=['/WJetsToLNu_0J_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM'],
    n_files=56,
    n_events=183585526.0, # this n_events is the gensumwt
    aux={'n_events': 183585526} # n_events in aux is the nEvents produced
)
cpn.add_dataset(
    name='wj_1j_amcatnlo',
    id=18150303,
    is_data=False,
    processes=[procs.w_lnu_1j],
    keys=['/WJetsToLNu_1J_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM'],
    n_files=138,
    n_events=183585526.0, # this n_events is the gensumwt
    aux={'n_events': 183585526} # n_events in aux is the nEvents produced
)
cpn.add_dataset(
    name='wj_2j_amcatnlo',
    id=18150304,
    is_data=False,
    processes=[procs.w_lnu_2j],
    keys=['/WJetsToLNu_2J_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM'],
    n_files=146,
    n_events=183585526.0, # this n_events is the gensumwt
    aux={'n_events': 183585526} # n_events in aux is the nEvents produced
)


# LO
cpn.add_dataset(
    name='wj_incl_madgraph',
    id=18150311,
    is_data=False,
    processes=[procs.w_lnu],
    keys=['/WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v2/NANOAODSIM'],
    n_files=81,
    n_events=183585526.0, # this n_events is the gensumwt
    aux={'n_events': 183585526} # n_events in aux is the nEvents produced
)
