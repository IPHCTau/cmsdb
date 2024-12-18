# coding: utf-8

"""
HH -> bbWW datasets for the 2023 pre-BPix data-taking campaign
"""

from order import DatasetInfo

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2023_preBPix_nano_v13 import campaign_run3_2023_preBPix_nano_v13 as cpn

#
# ggf, HH -> bbVV
#

cpn.add_dataset(
    name="hh_ggf_hbb_hvv_kl1_kt1_powheg",
    id=14961537,
    processes=[procs.hh_ggf_hbb_hvv_kl1_kt1],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/GluGlutoHHto2B2V_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv13-133X_mcRun3_2023_realistic_ForNanov13_v1-v1/NANOAODSIM",  # noqa
            ],
            n_files=36,
            n_events=666665,
        ),
    ),
)
cpn.add_dataset(
    name="hh_ggf_hbb_hvv_kl0_kt1_powheg",
    id=14961498,
    processes=[procs.hh_ggf_hbb_hvv_kl0_kt1],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/GluGlutoHHto2B2V_kl-0p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv13-133X_mcRun3_2023_realistic_ForNanov13_v1-v2/NANOAODSIM",  # noqa
            ],
            n_files=136,
            n_events=660790,
        ),
    ),
)
cpn.add_dataset(
    name="hh_ggf_hbb_hvv_kl5_kt1_powheg",
    id=14960790,
    processes=[procs.hh_ggf_hbb_hvv_kl5_kt1],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/GluGlutoHHto2B2V_kl-5p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv13-133X_mcRun3_2023_realistic_ForNanov13_v1-v2/NANOAODSIM",  # noqa
            ],
            n_files=133,
            n_events=664199,
        ),
    ),
)
cpn.add_dataset(
    name="hh_ggf_hbb_hvv2l2nu_kl1_kt1_powheg",
    id=14965386,
    processes=[procs.hh_ggf_hbb_hvv2l2nu_kl1_kt1],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/GluGlutoHHto2B2Vto2L2Nu_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv13-133X_mcRun3_2023_realistic_ForNanov13_v1-v1/NANOAODSIM",  # noqa
            ],
            n_files=32,
            n_events=266483,
        ),
    ),
)
cpn.add_dataset(
    name="hh_ggf_hbb_hvv2l2nu_kl0_kt1_powheg",
    id=14965871,
    processes=[procs.hh_ggf_hbb_hvv2l2nu_kl0_kt1],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/GluGlutoHHto2B2Vto2L2Nu_kl-0p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv13-133X_mcRun3_2023_realistic_ForNanov13_v1-v1/NANOAODSIM",  # noqa
            ],
            n_files=55,
            n_events=266667,
        ),
    ),
)
cpn.add_dataset(
    name="hh_ggf_hbb_hvv2l2nu_kl5_kt1_powheg",
    id=14964739,
    processes=[procs.hh_ggf_hbb_hvv2l2nu_kl5_kt1],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/GluGlutoHHto2B2Vto2L2Nu_kl-5p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv13-133X_mcRun3_2023_realistic_ForNanov13_v1-v2/NANOAODSIM",  # noqa
            ],
            n_files=35,
            n_events=265777,
        ),
    ),
)
cpn.add_dataset(
    name="hh_ggf_hbb_hvvqqlnu_kl1_kt1_powheg",
    id=14960633,
    processes=[procs.hh_ggf_hbb_hvvqqlnu_kl1_kt1],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/GluGlutoHHto2B2WtoLNu2Q_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv13-133X_mcRun3_2023_realistic_ForNanov13_v1-v2/NANOAODSIM",  # noqa
            ],
            n_files=48,
            n_events=265445,
        ),
    ),
)
cpn.add_dataset(
    name="hh_ggf_hbb_hvvqqlnu_kl5_kt1_powheg",
    id=14961800,
    processes=[procs.hh_ggf_hbb_hvvqqlnu_kl5_kt1],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/GluGlutoHHto2B2WtoLNu2Q_kl-5p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv13-133X_mcRun3_2023_realistic_ForNanov13_v1-v2/NANOAODSIM",  # noqa
            ],
            n_files=39,
            n_events=266232,
        ),
    ),
)
cpn.add_dataset(
    name="hh_ggf_hbb_hvvqqlnu_kl0_kt1_powheg",
    id=14965498,
    processes=[procs.hh_ggf_hbb_hvvqqlnu_kl0_kt1],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/GluGlutoHHto2B2WtoLNu2Q_kl-0p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv13-133X_mcRun3_2023_realistic_ForNanov13_v1-v2/NANOAODSIM",  # noqa
            ],
            n_files=41,
            n_events=265860,
        ),
    ),
)

#
# vbf, HH -> bbVV
#

cpn.add_dataset(
    name="hh_vbf_hbb_hvv_kv1_k2v1_kl1_madgraph",
    id=14964020,
    processes=[procs.hh_vbf_hbb_hvv_kv1_k2v1_kl1],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/VBFHHto2B2V_CV_1_C2V_1_C3_1_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23NanoAODv13-133X_mcRun3_2023_realistic_ForNanov13_v1-v2/NANOAODSIM",  # noqa
            ],
            n_files=9,
            n_events=660666,
        ),
    ),
)
cpn.add_dataset(
    name="hh_vbf_hbb_hvv_kv1_k2v0_kl1_madgraph",
    id=14961132,
    processes=[procs.hh_vbf_hbb_hvv_kv1_k2v0_kl1],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/VBFHHto2B2V_CV_1_C2V_0_C3_1_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23NanoAODv13-133X_mcRun3_2023_realistic_ForNanov13_v1-v2/NANOAODSIM",  # noqa
            ],
            n_files=3,
            n_events=666664,
        ),
    ),
)
cpn.add_dataset(
    name="hh_vbf_hbb_hvv_kv1p74_k2v1p37_kl14p4_madgraph",
    id=14966842,
    processes=[procs.hh_vbf_hbb_hvv_kv1p74_k2v1p37_kl14p4],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/VBFHHto2B2V_CV_1p74_C2V_1p37_C3_14p4_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23NanoAODv13-133X_mcRun3_2023_realistic_ForNanov13_v1-v2/NANOAODSIM",  # noqa
            ],
            n_files=20,
            n_events=654665,
        ),
    ),
)
cpn.add_dataset(
    name="hh_vbf_hbb_hvv_kvm0p758_k2v1p44_klm19p3_madgraph",
    id=14964514,
    processes=[procs.hh_vbf_hbb_hvv_kvm0p758_k2v1p44_klm19p3],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/VBFHHto2B2V_CV_m0p758_C2V_1p44_C3_m19p3_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23NanoAODv13-133X_mcRun3_2023_realistic_ForNanov13_v1-v2/NANOAODSIM",  # noqa
            ],
            n_files=3,
            n_events=660664,
        ),
    ),
)
cpn.add_dataset(
    name="hh_vbf_hbb_hvv_kvm1p6_k2v2p72_klm1p36_madgraph",
    id=14965345,
    processes=[procs.hh_vbf_hbb_hvv_kvm1p6_k2v2p72_klm1p36],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/VBFHHto2B2V_CV_m1p60_C2V_2p72_C3_m1p36_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23NanoAODv13-133X_mcRun3_2023_realistic_ForNanov13_v1-v2/NANOAODSIM",  # noqa
            ],
            n_files=5,
            n_events=663662,
        ),
    ),
)
cpn.add_dataset(
    name="hh_vbf_hbb_hvv_kvm0p012_k2v0p03_kl10p2_madgraph",
    id=14964327,
    processes=[procs.hh_vbf_hbb_hvv_kvm0p012_k2v0p03_kl10p2],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/VBFHHto2B2V_CV_m0p012_C2V_0p030_C3_10p2_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23NanoAODv13-133X_mcRun3_2023_realistic_ForNanov13_v1-v2/NANOAODSIM",  # noqa
            ],
            n_files=4,
            n_events=663663,
        ),
    ),
)
cpn.add_dataset(
    name="hh_vbf_hbb_hvv_kvm1p83_k2v3p57_klm3p39_madgraph",
    id=14964510,
    processes=[procs.hh_vbf_hbb_hvv_kvm1p83_k2v3p57_klm3p39],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/VBFHHto2B2V_CV_m1p83_C2V_3p57_C3_m3p39_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23NanoAODv13-133X_mcRun3_2023_realistic_ForNanov13_v1-v2/NANOAODSIM",  # noqa
            ],
            n_files=4,
            n_events=666663,
        ),
    ),
)
cpn.add_dataset(
    name="hh_vbf_hbb_hvv_kvm2p12_k2v3p87_klm5p96_madgraph",
    id=14966436,
    processes=[procs.hh_vbf_hbb_hvv_kvm2p12_k2v3p87_klm5p96],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/VBFHHto2B2V_CV_m2p12_C2V_3p87_C3_m5p96_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23NanoAODv13-133X_mcRun3_2023_realistic_ForNanov13_v1-v2/NANOAODSIM",  # noqa
            ],
            n_files=23,
            n_events=663665,
        ),
    ),
)
cpn.add_dataset(
    name="hh_vbf_hbb_hvv_kvm0p962_k2v0p959_klm1p43_madgraph",
    id=14967716,
    processes=[procs.hh_vbf_hbb_hvv_kvm0p962_k2v0p959_klm1p43],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/VBFHHto2B2V_CV_m0p962_C2V_0p959_C3_m1p43_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23NanoAODv13-133X_mcRun3_2023_realistic_ForNanov13_v1-v2/NANOAODSIM",  # noqa
            ],
            n_files=7,
            n_events=651662,
        ),
    ),
)
cpn.add_dataset(
    name="hh_vbf_hbb_hvv_kvm1p21_k2v1p94_klm0p94_madgraph",
    id=14966841,
    processes=[procs.hh_vbf_hbb_hvv_kvm1p21_k2v1p94_klm0p94],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/VBFHHto2B2V_CV_m1p21_C2V_1p94_C3_m0p94_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23NanoAODv13-133X_mcRun3_2023_realistic_ForNanov13_v1-v2/NANOAODSIM",  # noqa
            ],
            n_files=20,
            n_events=663664,
        ),
    ),
)
cpn.add_dataset(
    name="hh_vbf_hbb_hvv2l2nu_kv1_k2v1_kl1_madgraph",
    id=14965471,
    processes=[procs.hh_vbf_hbb_hvv2l2nu_kv1_k2v1_kl1],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/VBFHHto2B2Vto2L2Nu_CV_1_C2V_1_C3_1_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23NanoAODv13-133X_mcRun3_2023_realistic_ForNanov13_v1-v2/NANOAODSIM",  # noqa
            ],
            n_files=6,
            n_events=260666,
        ),
    ),
)
cpn.add_dataset(
    name="hh_vbf_hbb_hvv2l2nu_kv1_k2v0_kl1_madgraph",
    id=14964660,
    processes=[procs.hh_vbf_hbb_hvv2l2nu_kv1_k2v0_kl1],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/VBFHHto2B2Vto2L2Nu_CV_1_C2V_0_C3_1_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23NanoAODv13-133X_mcRun3_2023_realistic_ForNanov13_v1-v2/NANOAODSIM",  # noqa
            ],
            n_files=2,
            n_events=263666,
        ),
    ),
)
cpn.add_dataset(
    name="hh_vbf_hbb_hvv2l2nu_kvm1p21_k2v1p94_klm0p94_madgraph",
    id=14966287,
    processes=[procs.hh_vbf_hbb_hvv2l2nu_kvm1p21_k2v1p94_klm0p94],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/VBFHHto2B2Vto2L2Nu_CV_m1p21_C2V_1p94_C3_m0p94_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23NanoAODv13-133X_mcRun3_2023_realistic_ForNanov13_v1-v2/NANOAODSIM",  # noqa
            ],
            n_files=12,
            n_events=266666,
        ),
    ),
)
cpn.add_dataset(
    name="hh_vbf_hbb_hvv2l2nu_kvm0p758_k2v1p44_klm19p3_madgraph",
    id=14962862,
    processes=[procs.hh_vbf_hbb_hvv2l2nu_kvm0p758_k2v1p44_klm19p3],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/VBFHHto2B2Vto2L2Nu_CV_m0p758_C2V_1p44_C3_m19p3_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23NanoAODv13-133X_mcRun3_2023_realistic_ForNanov13_v1-v2/NANOAODSIM",  # noqa
            ],
            n_files=11,
            n_events=260666,
        ),
    ),
)
cpn.add_dataset(
    name="hh_vbf_hbb_hvv2l2nu_kvm1p83_k2v3p57_klm3p39_madgraph",
    id=14968359,
    processes=[procs.hh_vbf_hbb_hvv2l2nu_kvm1p83_k2v3p57_klm3p39],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/VBFHHto2B2Vto2L2Nu_CV_m1p83_C2V_3p57_C3_m3p39_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23NanoAODv13-133X_mcRun3_2023_realistic_ForNanov13_v1-v2/NANOAODSIM",  # noqa
            ],
            n_files=6,
            n_events=266667,
        ),
    ),
)
cpn.add_dataset(
    name="hh_vbf_hbb_hvv2l2nu_kvm1p6_k2v2p72_klm1p36_madgraph",
    id=14964575,
    processes=[procs.hh_vbf_hbb_hvv2l2nu_kvm1p6_k2v2p72_klm1p36],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/VBFHHto2B2Vto2L2Nu_CV_m1p60_C2V_2p72_C3_m1p36_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23NanoAODv13-133X_mcRun3_2023_realistic_ForNanov13_v1-v2/NANOAODSIM",  # noqa
            ],
            n_files=2,
            n_events=263666,
        ),
    ),
)
cpn.add_dataset(
    name="hh_vbf_hbb_hvv2l2nu_kvm0p012_k2v0p03_kl10p2_madgraph",
    id=14964869,
    processes=[procs.hh_vbf_hbb_hvv2l2nu_kvm0p012_k2v0p03_kl10p2],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/VBFHHto2B2Vto2L2Nu_CV_m0p012_C2V_0p030_C3_10p2_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23NanoAODv13-133X_mcRun3_2023_realistic_ForNanov13_v1-v2/NANOAODSIM",  # noqa
            ],
            n_files=3,
            n_events=266667,
        ),
    ),
)
cpn.add_dataset(
    name="hh_vbf_hbb_hvv2l2nu_kvm0p962_k2v0p959_klm1p43_madgraph",
    id=14967621,
    processes=[procs.hh_vbf_hbb_hvv2l2nu_kvm0p962_k2v0p959_klm1p43],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/VBFHHto2B2Vto2L2Nu_CV_m0p962_C2V_0p959_C3_m1p43_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23NanoAODv13-133X_mcRun3_2023_realistic_ForNanov13_v1-v2/NANOAODSIM",  # noqa
            ],
            n_files=4,
            n_events=266666,
        ),
    ),
)
cpn.add_dataset(
    name="hh_vbf_hbb_hvv2l2nu_kvm2p12_k2v3p87_klm5p96_madgraph",
    id=14966240,
    processes=[procs.hh_vbf_hbb_hvv2l2nu_kvm2p12_k2v3p87_klm5p96],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/VBFHHto2B2Vto2L2Nu_CV_m2p12_C2V_3p87_C3_m5p96_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23NanoAODv13-133X_mcRun3_2023_realistic_ForNanov13_v1-v2/NANOAODSIM",  # noqa
            ],
            n_files=6,
            n_events=266666,
        ),
    ),
)
cpn.add_dataset(
    name="hh_vbf_hbb_hvv2l2nu_kv1p74_k2v1p37_kl14p4_madgraph",
    id=14967615,
    processes=[procs.hh_vbf_hbb_hvv2l2nu_kv1p74_k2v1p37_kl14p4],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/VBFHHto2B2Vto2L2Nu_CV_1p74_C2V_1p37_C3_14p4_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23NanoAODv13-133X_mcRun3_2023_realistic_ForNanov13_v1-v2/NANOAODSIM",  # noqa
            ],
            n_files=9,
            n_events=266666,
        ),
    ),
)
cpn.add_dataset(
    name="hh_vbf_hbb_hvvqqlnu_kv1_k2v1_kl1_madgraph",
    id=14963814,
    processes=[procs.hh_vbf_hbb_hvvqqlnu_kv1_k2v1_kl1],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/VBFHHto2B2WtoLNu2Q_CV_1_C2V_1_C3_1_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23NanoAODv13-133X_mcRun3_2023_realistic_ForNanov13_v1-v2/NANOAODSIM",  # noqa
            ],
            n_files=2,
            n_events=266665,
        ),
    ),
)
cpn.add_dataset(
    name="hh_vbf_hbb_hvvqqlnu_kv1_k2v0_kl1_madgraph",
    id=14964381,
    processes=[procs.hh_vbf_hbb_hvvqqlnu_kv1_k2v0_kl1],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/VBFHHto2B2WtoLNu2Q_CV_1_C2V_0_C3_1_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23NanoAODv13-133X_mcRun3_2023_realistic_ForNanov13_v1-v2/NANOAODSIM",  # noqa
            ],
            n_files=3,
            n_events=266663,
        ),
    ),
)
cpn.add_dataset(
    name="hh_vbf_hbb_hvvqqlnu_kvm2p12_k2v3p87_klm5p96_madgraph",
    id=14966356,
    processes=[procs.hh_vbf_hbb_hvvqqlnu_kvm2p12_k2v3p87_klm5p96],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/VBFHHto2B2WtoLNu2Q_CV_m2p12_C2V_3p87_C3_m5p96_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23NanoAODv13-133X_mcRun3_2023_realistic_ForNanov13_v1-v2/NANOAODSIM",  # noqa
            ],
            n_files=10,
            n_events=263665,
        ),
    ),
)
cpn.add_dataset(
    name="hh_vbf_hbb_hvvqqlnu_kvm1p6_k2v2p72_klm1p36_madgraph",
    id=14966839,
    processes=[procs.hh_vbf_hbb_hvvqqlnu_kvm1p6_k2v2p72_klm1p36],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/VBFHHto2B2WtoLNu2Q_CV_m1p60_C2V_2p72_C3_m1p36_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23NanoAODv13-133X_mcRun3_2023_realistic_ForNanov13_v1-v2/NANOAODSIM",  # noqa
            ],
            n_files=17,
            n_events=266663,
        ),
    ),
)
cpn.add_dataset(
    name="hh_vbf_hbb_hvvqqlnu_kvm1p21_k2v1p94_klm0p94_madgraph",
    id=14966389,
    processes=[procs.hh_vbf_hbb_hvvqqlnu_kvm1p21_k2v1p94_klm0p94],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/VBFHHto2B2WtoLNu2Q_CV_m1p21_C2V_1p94_C3_m0p94_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23NanoAODv13-133X_mcRun3_2023_realistic_ForNanov13_v1-v2/NANOAODSIM",  # noqa
            ],
            n_files=7,
            n_events=266664,
        ),
    ),
)
cpn.add_dataset(
    name="hh_vbf_hbb_hvvqqlnu_kvm0p962_k2v0p959_klm1p43_madgraph",
    id=14966267,
    processes=[procs.hh_vbf_hbb_hvvqqlnu_kvm0p962_k2v0p959_klm1p43],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/VBFHHto2B2WtoLNu2Q_CV_m0p962_C2V_0p959_C3_m1p43_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23NanoAODv13-133X_mcRun3_2023_realistic_ForNanov13_v1-v2/NANOAODSIM",  # noqa
            ],
            n_files=10,
            n_events=266664,
        ),
    ),
)
cpn.add_dataset(
    name="hh_vbf_hbb_hvvqqlnu_kv1p74_k2v1p37_kl14p4_madgraph",
    id=14968351,
    processes=[procs.hh_vbf_hbb_hvvqqlnu_kv1p74_k2v1p37_kl14p4],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/VBFHHto2B2WtoLNu2Q_CV_1p74_C2V_1p37_C3_14p4_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23NanoAODv13-133X_mcRun3_2023_realistic_ForNanov13_v1-v2/NANOAODSIM",  # noqa
            ],
            n_files=5,
            n_events=266663,
        ),
    ),
)
cpn.add_dataset(
    name="hh_vbf_hbb_hvvqqlnu_kvm1p83_k2v3p57_klm3p39_madgraph",
    id=14964446,
    processes=[procs.hh_vbf_hbb_hvvqqlnu_kvm1p83_k2v3p57_klm3p39],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/VBFHHto2B2WtoLNu2Q_CV_m1p83_C2V_3p57_C3_m3p39_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23NanoAODv13-133X_mcRun3_2023_realistic_ForNanov13_v1-v2/NANOAODSIM",  # noqa
            ],
            n_files=2,
            n_events=266663,
        ),
    ),
)
cpn.add_dataset(
    name="hh_vbf_hbb_hvvqqlnu_kvm0p012_k2v0p03_kl10p2_madgraph",
    id=14966290,
    processes=[procs.hh_vbf_hbb_hvvqqlnu_kvm0p012_k2v0p03_kl10p2],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/VBFHHto2B2WtoLNu2Q_CV_m0p012_C2V_0p030_C3_10p2_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23NanoAODv13-133X_mcRun3_2023_realistic_ForNanov13_v1-v2/NANOAODSIM",  # noqa
            ],
            n_files=4,
            n_events=266661,
        ),
    ),
)
cpn.add_dataset(
    name="hh_vbf_hbb_hvvqqlnu_kvm0p758_k2v1p44_klm19p3_madgraph",
    id=14961035,
    processes=[procs.hh_vbf_hbb_hvvqqlnu_kvm0p758_k2v1p44_klm19p3],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/VBFHHto2B2WtoLNu2Q_CV_m0p758_C2V_1p44_C3_m19p3_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23NanoAODv13-133X_mcRun3_2023_realistic_ForNanov13_v1-v2/NANOAODSIM",  # noqa
            ],
            n_files=7,
            n_events=260665,
        ),
    ),
)
