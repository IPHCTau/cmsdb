# dy.py
# Link: /store/user/ksavva/data/HLepRare/skim_2024_v2/Run3_2022
# ID: 181502XX

import cmsdb.processes as procs
from cmsdb.campaigns.run2_2018_taupol_nano_v15 import campaign_run2_2018_taupol_nano_v15 as cpn


# signal for tau polarization analysis
cpn.add_dataset(
    name='dy_2tau_m50_amcatnlo',
    id=18150201,
    is_data=False,
    processes=[procs.dy_2tau_m50toinf_nj],
    #keys=['/DYJetsToTauTau_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8-photos/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM'],
    keys=['/DYJetsToTauTau_M-50_TuneCP5_13TeV'],
    n_files=18,
    n_events=25697815101.5459, # this n_events is the gensumwt
    aux={'is_signal': False, 'n_events': 11315669} # n_events in aux is the nEvents produced
)


# lepton flavor inclusive DY samples (njet inclusive) - LO
cpn.add_dataset(
    name='dy_lep_m50_madgraph',
    id=18150210,
    is_data=False,
    processes=[procs.dy_m50toinf],
    keys=['/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v2/NANOAODSIM',
          '/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1_ext1-v1/NANOAODSIM'],
    n_files=84 + 83,
    n_events=115297314.0, # this n_events is the gensumwt 
    aux={'n_events': 173189950} # n_events in aux is the nEvents produced
)


# lepton flavor inclusive DY samples (njet inclusive) - NLO
cpn.add_dataset(
    name='dy_lep_m50_amcatnlo',
    id=18150220,
    is_data=False,
    processes=[procs.dy_m50toinf],
    keys=['/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM'],
    n_files=163,
    n_events=115297314.0, # this n_events is the gensumwt 
    aux={'n_events': 173189950} # n_events in aux is the nEvents produced
)

# lepton flavor inclusive DY samples (njet exclusive)
cpn.add_dataset(
    name='dy_lep_m50_0j_amcatnlo',
    id=18150221,
    is_data=False,
    processes=[procs.dy_m50toinf_0j],
    keys=['/DYJetsToLL_0J_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM'],
    n_files=71,
    n_events=77502776.0, # this n_events is the gensumwt
    aux={'n_events': 97176340} # n_events in aux is the nEvents produced 
)
cpn.add_dataset(
    name='dy_lep_m50_1j_amcatnlo',
    id=18150222,
    is_data=False,
    processes=[procs.dy_m50toinf_1j],
    keys=['/DYJetsToLL_1J_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM'],
    n_files=91,
    n_events=77502776.0, # this n_events is the gensumwt
    aux={'n_events': 97176340} # n_events in aux is the nEvents produced 
)
cpn.add_dataset(
    name='dy_lep_m50_2j_amcatnlo',
    id=18150223,
    is_data=False,
    processes=[procs.dy_m50toinf_2j],
    keys=['/DYJetsToLL_2J_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM'],
    n_files=47,
    n_events=77502776.0, # this n_events is the gensumwt
    aux={'n_events': 97176340} # n_events in aux is the nEvents produced 
)

