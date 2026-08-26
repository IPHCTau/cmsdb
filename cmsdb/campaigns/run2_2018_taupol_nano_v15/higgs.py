# signal.py
# Link: /store/user/ksavva/data/HLepRare/skim_2024_v2/Run3_2022
# ID: 181506XX

import cmsdb.processes as procs
from cmsdb.campaigns.run2_2018_taupol_nano_v15 import campaign_run2_2018_taupol_nano_v15 as cpn



cpn.add_dataset(
    name='h_ggf_htt_powheg',
    id=18150601,
    is_data=False,
    processes=[procs.h_ggf_htt],
    keys=['/GluGluHToTauTau_M125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM'],
    n_files=12,
    n_events=585054.0, # this n_events is the gensumwt
    aux={'is_signal': True, 'n_events': 1038456} # n_events in aux is the nEvents produced
)
cpn.add_dataset(
    name='zh_htt_powheg',
    id=18150602,
    is_data=False,
    processes=[procs.zh_htt],
    keys=['/ZHToTauTau_M125_CP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM'],
    n_files=7,
    n_events=613598.0, # this n_events is the gensumwt
    aux={'is_signal': True, 'n_events': 613598} # n_events in aux is the nEvents produced
)
cpn.add_dataset(
    name='wph_htt_powheg',
    id=18150603,
    is_data=False,
    processes=[procs.wph_htt],
    keys=['/WplusHToTauTau_M125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM'],
    n_files=6,
    n_events=716466.0, # this n_events is the gensumwt
    aux={'is_signal': True, 'n_events': 750698} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='wmh_htt_powheg',
    id=18150604,
    is_data=False,
    processes=[procs.wmh_htt],
    keys=['/WminusHToTauTau_M125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM'],
    n_files=7,
    n_events=431839.0, # this n_events is the gensumwt
    aux={'is_signal': True, 'n_events': 452083} # n_events in aux is the nEvents produced
)
