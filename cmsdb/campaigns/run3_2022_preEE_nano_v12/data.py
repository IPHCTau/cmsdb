# coding: utf-8

"""
CMS datasets from the 2022 pre-EE data-taking campaign
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2022_preEE_nano_v12 import campaign_run3_2022_preEE_nano_v12 as cpn


#
# Muon
#


cpn.add_dataset(
    name="data_mu_c",
    id=14784127,
    is_data=True,
    processes=[procs.data_mu],
    keys=[
        "/Muon/Run2022C-22Sep2023-v1/NANOAOD",  # noqa
    ],
    n_files=124,
    n_events=138427345,
    aux={
        "era": "C",
        "jec_era": "RunCD",
    },
)

cpn.add_dataset(
    name="data_mu_d",
    id=14783357,
    is_data=True,
    processes=[procs.data_mu],
    keys=[
        "/Muon/Run2022D-22Sep2023-v1/NANOAOD",  # noqa
    ],
    n_files=82,
    n_events=75468381,
    aux={
        "era": "D",
        "jec_era": "RunCD",
    },
)


#
# E/Gamma
#


cpn.add_dataset(
    name="data_egamma_a",
    id=14783268,
    is_data=True,
    processes=[procs.data_egamma],
    keys=[
        "/EGamma/Run2022A-22Sep2023-v1/NANOAOD",  # noqa
    ],
    n_files=5,
    n_events=186,
    aux={
        "era": "A",
    },
)

cpn.add_dataset(
    name="data_egamma_b",
    id=14826835,
    is_data=True,
    processes=[procs.data_egamma],
    keys=[
        "/EGamma/Run2022B-22Sep2023-v2/NANOAOD",  # noqa
    ],
    n_files=14,
    n_events=11074301,
    aux={
        "era": "B",
    },
)

cpn.add_dataset(
    name="data_egamma_c",
    id=14784140,
    is_data=True,
    processes=[procs.data_egamma],
    keys=[
        "/EGamma/Run2022C-22Sep2023-v1/NANOAOD",  # noqa
    ],
    n_files=313,
    n_events=263689151,
    aux={
        "era": "C",
        "jec_era": "RunCD",
    },
)

cpn.add_dataset(
    name="data_egamma_d",
    id=14783299,
    is_data=True,
    processes=[procs.data_egamma],
    keys=[
        "/EGamma/Run2022D-22Sep2023-v1/NANOAOD",  # noqa
    ],
    n_files=109,
    n_events=89134996,
    aux={
        "era": "D",
        "jec_era": "RunCD",
    },
)


#
# MuonEG
#


cpn.add_dataset(
    name="data_muoneg_a",
    id=14783289,
    is_data=True,
    processes=[procs.data_muoneg],
    keys=[
        "/MuonEG/Run2022A-22Sep2023-v1/NANOAOD",  # noqa
    ],
    n_files=5,
    n_events=12,
    aux={
        "era": "A",
    },
)

cpn.add_dataset(
    name="data_muoneg_b",
    id=14784076,
    is_data=True,
    processes=[procs.data_muoneg],
    keys=[
        "/MuonEG/Run2022B-22Sep2023-v1/NANOAOD",  # noqa
    ],
    n_files=7,
    n_events=254803,
    aux={
        "era": "B",
    },
)

cpn.add_dataset(
    name="data_muoneg_c",
    id=14784125,
    is_data=True,
    processes=[procs.data_muoneg],
    keys=[
        "/MuonEG/Run2022C-22Sep2023-v1/NANOAOD",  # noqa
    ],
    n_files=28,
    n_events=15768439,
    aux={
        "era": "C",
        "jec_era": "RunCD",
    },
)

cpn.add_dataset(
    name="data_muoneg_d",
    id=14784209,
    is_data=True,
    processes=[procs.data_muoneg],
    keys=[
        "/MuonEG/Run2022D-22Sep2023-v1/NANOAOD",  # noqa
    ],
    n_files=16,
    n_events=8007031,
    aux={
        "era": "D",
        "jec_era": "RunCD",
    },
)

# Tau
cpn.add_dataset(
    name="data_tau_c",
    id=14784173,
    is_data=True,
    processes=[procs.data_tau],
    keys=[
        "/Tau/Run2022C-22Sep2023-v1/NANOAOD",  # noqa
    ],
    n_files=34,
    n_events=25875389,
    aux={
        "era": "C",
        "jec_era": "RunCD",
    },
)

cpn.add_dataset(
    name="data_tau_d",
    id=14783294,
    is_data=True,
    processes=[procs.data_tau],
    keys=[
        "/Tau/Run2022D-22Sep2023-v1/NANOAOD",  # noqa
    ],
    n_files=26,
    n_events=16686692,
    aux={
        "era": "D",
        "jec_era": "RunCD",
    },
)

# Jet/MET
cpn.add_dataset(
    name="data_met_c",
    id=14784135,
    is_data=True,
    processes=[procs.data_met],
    keys=[
        "/JetMET/Run2022C-22Sep2023-v1/NANOAOD",  # noqa
    ],
    n_files=206,
    n_events=169187457,
    aux={
        "era": "C",
        "jec_era": "RunCD",
    },
)

cpn.add_dataset(
    name="data_met_d",
    id=14809508,
    is_data=True,
    processes=[procs.data_met],
    keys=[
        "/JetMET/Run2022D-22Sep2023-v1/NANOAOD",  # noqa
    ],
    n_files=100,
    n_events=100853361,
    aux={
        "era": "D",
        "jec_era": "RunCD",
    },
)
