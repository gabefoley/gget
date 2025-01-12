import unittest
from gget.gget_info import info


class TestInfo(unittest.TestCase):
    maxDiff = None

    def test_info_WB_gene(self):
        df = info("WBGene00043981")
        # Drop NaN columns, since np.nan != np.nan
        result_to_test = df.dropna(axis=1).values.tolist()
        expected_result = [
            [
                "WBGene00043981",
                "Q5WRS0",
                "3565421",
                "caenorhabditis_elegans",
                "WBcel235",
                "aaim-1",
                "T14E8.4",
                [],
                "Protein aaim-1",
                "Uncharacterized protein [Source:NCBI gene (formerly Entrezgene);Acc:3565421]",
                "(Microbial infection) Promotes infection by microsporidian pathogens such as N.parisii in the early larval stages of development (PubMed:34994689). Involved in ensuring the proper orientation and location of the spore proteins of N.parisii during intestinal cell invasion (PubMed:34994689) Plays a role in promoting resistance to bacterial pathogens such as P.aeruginosa by inhibiting bacterial intestinal colonization",
                "Gene",
                "protein_coding",
                "T14E8.4.1.",
                "X",
                -1,
                6559466,
                6562428,
                ["T14E8.4.1"],
                ["protein_coding"],
                [unittest.mock.ANY],
                [-1],
                [6559466],
                [6562428],
            ]
        ]
        self.assertListEqual(result_to_test, expected_result)

    def test_info_WB_transcript(self):
        df = info("T14E8.4.1")
        # Drop NaN columns, since np.nan != np.nan
        result_to_test = df.dropna(axis=1).values.tolist()
        expected_result = [
            [
                "T14E8.4.1",
                ["Q5WRS0", "Q6RYS9"],
                "caenorhabditis_elegans",
                "WBcel235",
                ["aaim-1", "dop-3"],
                [],
                "WBGene00043981",
                ["Protein aaim-1", "Dopamine receptor 3"],
                [
                    "(Microbial infection) Promotes infection by microsporidian pathogens such as N.parisii in the early larval stages of development (PubMed:34994689). Involved in ensuring the proper orientation and location of the spore proteins of N.parisii during intestinal cell invasion (PubMed:34994689) Plays a role in promoting resistance to bacterial pathogens such as P.aeruginosa by inhibiting bacterial intestinal colonization",
                    "G-protein coupled receptor which binds to the neurotransmitter dopamine with high affinity leading to the activation of an associated G-protein and downstream signaling pathways (PubMed:15378064, PubMed:16001968). Couples to G-proteins to inhibit adenylate cyclase (AC) activity and cAMP production (PubMed:15378064, PubMed:16001968). Antagonizes the D1-like dopamine receptor dop-1 to negatively regulate the rate of locomotion (PubMed:15378064). In GABAergic, RIC, and SIA neurons, antagonizes the function of dop-1 to play a role in behavioral plasticity and regulate the decision-making process when conflicting alternatives are present (PubMed:25536037). Antagonizes octopamine signaling in response to food by promoting the dopamine-mediated suppression of crh-1/CREB1 transcription factor activation in cholinergic SIA neurons (PubMed:19609300). This is most likely in association with the G(o)-alpha G-protein subunit goa-1 (PubMed:19609300). Promotes male mating behavior by antagonizing acetylcholine signaling to control the protrusion of copulatory spicules from the tail of males during hermaphrodite vulval location (PubMed:23166505)",
                ],
                "Transcript",
                "protein_coding",
                "X",
                -1,
                6559466,
                6562428,
                [
                    "T14E8.4.1.e1",
                    "T14E8.4.1.e2",
                    "T14E8.4.1.e3",
                    "T14E8.4.1.e4",
                    "T14E8.4.1.e5",
                    "T14E8.4.1.e6",
                    "T14E8.4.1.e7",
                    "T14E8.4.1.e8",
                    "T14E8.4.1.e9",
                ],
                [
                    6562330,
                    6562225,
                    6562110,
                    6561817,
                    6561252,
                    6560727,
                    6560492,
                    6560197,
                    6559466,
                ],
                [
                    6562428,
                    6562286,
                    6562183,
                    6562059,
                    6561378,
                    6561206,
                    6560671,
                    6560443,
                    6559667,
                ],
                [
                    "T14E8.4.1.e1",
                    "T14E8.4.1.e2",
                    "T14E8.4.1.e3",
                    "T14E8.4.1.e4",
                    "T14E8.4.1.e5",
                    "T14E8.4.1.e6",
                    "T14E8.4.1.e7",
                    "T14E8.4.1.e8",
                    "T14E8.4.1.e9",
                ],
                [
                    6562330,
                    6562225,
                    6562110,
                    6561817,
                    6561252,
                    6560727,
                    6560492,
                    6560197,
                    6559466,
                ],
                [
                    6562428,
                    6562286,
                    6562183,
                    6562059,
                    6561378,
                    6561206,
                    6560671,
                    6560443,
                    6559667,
                ],
            ]
        ]
        self.assertListEqual(result_to_test, expected_result)

    def test_info_FB_gene(self):
        df = info("FBgn0003656")
        # Drop NaN columns, since np.nan != np.nan
        result_to_test = df.dropna(axis=1).values.tolist()
        expected_result = [
            [
                "FBgn0003656",
                "Q9U969",
                "31716",
                "drosophila_melanogaster",
                "BDGP6.32",
                "sws",
                "sws",
                ["CG2212", "Dmel\\CG2212", "PNPLA6", "SWS", "Sws", "olfE"],
                "Neuropathy target esterase sws",
                "swiss cheese",
                "Phospholipase B that deacylates intracellular phosphatidylcholine (PtdCho), generating glycerophosphocholine (GroPtdCho). This deacylation occurs at both sn-2 and sn-1 positions of PtdCho. Its specific chemical modification by certain organophosphorus (OP) compounds leads to distal axonopathy. Plays a role in the signaling mechanism between neurons and glia that regulates glia wrapping during development of the adult brain. Essential for membrane lipid homeostasis and cell survival in both neurons and glia of the adult brain",
                "Enables lysophospholipase activity and protein kinase A catalytic subunit binding activity. Involved in several processes, including negative regulation of cAMP-dependent protein kinase activity; photoreceptor cell maintenance; and sensory perception of smell. Located in endoplasmic reticulum membrane and plasma membrane. Is expressed in adult head and interface glial cell. Used to study blindness; cerebellar ataxia; hereditary spastic paraplegia; and neurodegenerative disease. Human ortholog(s) of this gene implicated in Boucher-Neuhauser syndrome; Laurence-Moon syndrome; Oliver-McFarlane syndrome; and hereditary spastic paraplegia 39. Orthologous to human PNPLA6 (patatin like phospholipase domain containing 6) and PNPLA7 (patatin like phospholipase domain containing 7). [provided by Alliance of Genome Resources, Apr 2022]",
                "Gene",
                "protein_coding",
                "FBtr0071125.",
                "X",
                -1,
                7956820,
                7968236,
                ["FBtr0301675", "FBtr0071125", "FBtr0071126"],
                ["protein_coding", "protein_coding", "protein_coding"],
                ["sws-RC", "sws-RA", "sws-RB"],
                [-1, -1, -1],
                [7956820, 7956820, 7956820],
                [7968236, 7968236, 7959369],
            ]
        ]
        self.assertListEqual(result_to_test, expected_result)

    def test_info_gene(self):
        df = info("ENSMUSG00000000001")
        # Drop NaN columns, since np.nan != np.nan
        result_to_test = df.dropna(axis=1).values.tolist()
        expected_result = [
            [
                "ENSMUSG00000000001.5",
                "Q9DC51",
                "14679",
                "mus_musculus",
                "GRCm39",
                "Gnai3",
                "Gnai3",
                ["Galphai3", "Gnai-3", "Hg1a"],
                "Guanine nucleotide-binding protein G(i) subunit alpha-3",
                "guanine nucleotide binding protein (G protein), alpha inhibiting 3 [Source:MGI Symbol;Acc:MGI:95773]",
                "Heterotrimeric guanine nucleotide-binding proteins (G proteins) function as transducers downstream of G protein-coupled receptors (GPCRs) in numerous signaling cascades. The alpha chain contains the guanine nucleotide binding site and alternates between an active, GTP-bound state and an inactive, GDP-bound state. Signaling by an activated GPCR promotes GDP release and GTP binding. The alpha subunit has a low GTPase activity that converts bound GTP to GDP, thereby terminating the signal. Both GDP release and GTP hydrolysis are modulated by numerous regulatory proteins. Signaling is mediated via effector proteins, such as adenylate cyclase. Inhibits adenylate cyclase activity, leading to decreased intracellular cAMP levels. Stimulates the activity of receptor-regulated K(+) channels. The active GTP-bound form prevents the association of RGS14 with centrosomes and is required for the translocation of RGS14 from the cytoplasm to the plasma membrane. May play a role in cell division",
                "Predicted to enable several functions, including G-protein beta/gamma-subunit complex binding activity; GDP binding activity; and GTPase activating protein binding activity. Predicted to be involved in several processes, including positive regulation of NAD(P)H oxidase activity; positive regulation of superoxide anion generation; and positive regulation of vascular associated smooth muscle cell proliferation. Predicted to act upstream of or within G protein-coupled receptor signaling pathway. Located in Golgi apparatus. Is expressed in early conceptus; inner ear; and oocyte. Orthologous to human GNAI3 (G protein subunit alpha i3). [provided by Alliance of Genome Resources, Apr 2022]",
                "Gene",
                "protein_coding",
                "ENSMUST00000000001.5",
                "3",
                -1,
                108014596,
                108053462,
                ["ENSMUST00000000001.5"],
                ["protein_coding"],
                ["Gnai3-201"],
                [-1],
                [108014596],
                [108053462],
            ]
        ]
        self.assertListEqual(result_to_test, expected_result)

    def test_info_gene_list_non_model(self):
        df = info(
            ["ENSMMUG00000054106.1", "ENSMMUG00000053116.1", "ENSMMUG00000021246.4"]
        )
        # Drop NaN columns, since np.nan != np.nan
        result_to_test = df.dropna(axis=1).values.tolist()
        expected_result = [
            [
                "ENSMMUG00000054106.1",
                "macaca_mulatta",
                "Mmul_10",
                [],
                "Gene",
                "lncRNA",
                "ENSMMUT00000080640.1",
                "8",
                1,
                64990191,
                65000159,
                ["ENSMMUT00000080640.1", "ENSMMUT00000100253.1"],
                ["lncRNA", "lncRNA"],
                [unittest.mock.ANY, unittest.mock.ANY],
                [1, 1],
                [64990191, 64993715],
                [65000159, 64999625],
            ],
            [
                "ENSMMUG00000053116.1",
                "macaca_mulatta",
                "Mmul_10",
                [],
                "Gene",
                "protein_coding",
                "ENSMMUT00000091015.1",
                "3",
                -1,
                111461994,
                111475279,
                ["ENSMMUT00000091015.1"],
                ["protein_coding"],
                [unittest.mock.ANY],
                [-1],
                [111461994],
                [111475279],
            ],
            [
                "ENSMMUG00000021246.4",
                "macaca_mulatta",
                "Mmul_10",
                ["HIGD1A"],
                "Gene",
                "protein_coding",
                "ENSMMUT00000029894.4",
                "2",
                -1,
                98646979,
                98755023,
                [
                    "ENSMMUT00000029893.4",
                    "ENSMMUT00000053619.2",
                    "ENSMMUT00000104418.1",
                    "ENSMMUT00000087615.1",
                    "ENSMMUT00000103912.1",
                    "ENSMMUT00000086824.1",
                    "ENSMMUT00000029894.4",
                    "ENSMMUT00000104481.1",
                    "ENSMMUT00000090481.1",
                    "ENSMMUT00000026408.4",
                ],
                [
                    "protein_coding",
                    "protein_coding",
                    "protein_coding",
                    "protein_coding",
                    "protein_coding",
                    "protein_coding",
                    "protein_coding",
                    "protein_coding",
                    "protein_coding",
                    "protein_coding",
                ],
                [
                    "CCDC13-201",
                    "CCDC13-202",
                    "CCDC13-203",
                    "CCDC13-204",
                    "CCDC13-205",
                    "CCDC13-206",
                    "CCDC13-207",
                    "CCDC13-208",
                    "CCDC13-209",
                    "CCDC13-210",
                ],
                [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
                [
                    98646979,
                    98646982,
                    98646984,
                    98646984,
                    98646985,
                    98662368,
                    98663259,
                    98690412,
                    98737900,
                    98738870,
                ],
                [
                    98655536,
                    98656674,
                    98688669,
                    98656968,
                    98656865,
                    98713982,
                    98746548,
                    98713982,
                    98755023,
                    98754684,
                ],
            ],
        ]

        self.assertEqual(result_to_test, expected_result)

    def test_info_transcript(self):
        df = info("ENSMUST00000000001.1")
        # Drop NaN columns, since np.nan != np.nan
        result_to_test = df.dropna(axis=1).values.tolist()
        expected_result = [
            [
                "ENSMUST00000000001.5",
                "Q9DC51",
                "14679",
                "mus_musculus",
                "GRCm39",
                "Gnai3",
                "Gnai3-201",
                ["Galphai3", "Gnai-3", "Hg1a"],
                "ENSMUSG00000000001",
                "Guanine nucleotide-binding protein G(i) subunit alpha-3",
                "Heterotrimeric guanine nucleotide-binding proteins (G proteins) function as transducers downstream of G protein-coupled receptors (GPCRs) in numerous signaling cascades. The alpha chain contains the guanine nucleotide binding site and alternates between an active, GTP-bound state and an inactive, GDP-bound state. Signaling by an activated GPCR promotes GDP release and GTP binding. The alpha subunit has a low GTPase activity that converts bound GTP to GDP, thereby terminating the signal. Both GDP release and GTP hydrolysis are modulated by numerous regulatory proteins. Signaling is mediated via effector proteins, such as adenylate cyclase. Inhibits adenylate cyclase activity, leading to decreased intracellular cAMP levels. Stimulates the activity of receptor-regulated K(+) channels. The active GTP-bound form prevents the association of RGS14 with centrosomes and is required for the translocation of RGS14 from the cytoplasm to the plasma membrane. May play a role in cell division",
                "Predicted to enable several functions, including G-protein beta/gamma-subunit complex binding activity; GDP binding activity; and GTPase activating protein binding activity. Predicted to be involved in several processes, including positive regulation of NAD(P)H oxidase activity; positive regulation of superoxide anion generation; and positive regulation of vascular associated smooth muscle cell proliferation. Predicted to act upstream of or within G protein-coupled receptor signaling pathway. Located in Golgi apparatus. Is expressed in early conceptus; inner ear; and oocyte. Orthologous to human GNAI3 (G protein subunit alpha i3). [provided by Alliance of Genome Resources, Apr 2022]",
                "Transcript",
                "protein_coding",
                "3",
                -1,
                108014596,
                108053462,
                [
                    "ENSMUSE00000334714.4",
                    "ENSMUSE00000276500.2",
                    "ENSMUSE00000276490.2",
                    "ENSMUSE00000276482.2",
                    "ENSMUSE00000565003.2",
                    "ENSMUSE00000565001.2",
                    "ENSMUSE00000565000.2",
                    "ENSMUSE00000404895.2",
                    "ENSMUSE00000363317.3",
                ],
                [
                    108053204,
                    108031111,
                    108030858,
                    108025617,
                    108023079,
                    108019789,
                    108019251,
                    108016719,
                    108014596,
                ],
                [
                    108053462,
                    108031153,
                    108030999,
                    108025774,
                    108023207,
                    108019918,
                    108019404,
                    108016928,
                    108016632,
                ],
                [
                    "ENSMUSE00000334714.4",
                    "ENSMUSE00000276500.2",
                    "ENSMUSE00000276490.2",
                    "ENSMUSE00000276482.2",
                    "ENSMUSE00000565003.2",
                    "ENSMUSE00000565001.2",
                    "ENSMUSE00000565000.2",
                    "ENSMUSE00000404895.2",
                    "ENSMUSE00000363317.3",
                ],
                [
                    108053204,
                    108031111,
                    108030858,
                    108025617,
                    108023079,
                    108019789,
                    108019251,
                    108016719,
                    108014596,
                ],
                [
                    108053462,
                    108031153,
                    108030999,
                    108025774,
                    108023207,
                    108019918,
                    108019404,
                    108016928,
                    108016632,
                ],
            ]
        ]
        self.assertListEqual(result_to_test, expected_result)

    def test_info_mix(self):
        df = info(["ENSTGUT00000027003.1", "ENSG00000169174"])
        # Drop NaN columns, since np.nan != np.nan
        result_to_test = df.dropna(axis=1).values.tolist()
        expected_result = [
            [
                "ENSTGUT00000027003.1",
                "A0A674GVD2",
                "taeniopygia_guttata",
                "bTaeGut1_v1.p",
                "FUNDC1",
                "FUNDC1-202",
                [],
                "",
                "Transcript",
                "protein_coding",
                "1",
                -1,
                107513786,
                107526965,
            ],
            [
                "ENSG00000169174.11",
                "Q8NBP7",
                "homo_sapiens",
                "GRCh38",
                "PCSK9",
                "PCSK9",
                ["FH3", "FHCL3", "HCHOLA3", "LDLCQ1", "NARC-1", "NARC1", "PC9"],
                "Crucial player in the regulation of plasma cholesterol homeostasis. Binds to low-density lipid receptor family members: low density lipoprotein receptor (LDLR), very low density lipoprotein receptor (VLDLR), apolipoprotein E receptor (LRP1/APOER) and apolipoprotein receptor 2 (LRP8/APOER2), and promotes their degradation in intracellular acidic compartments (PubMed:18039658). Acts via a non-proteolytic mechanism to enhance the degradation of the hepatic LDLR through a clathrin LDLRAP1/ARH-mediated pathway. May prevent the recycling of LDLR from endosomes to the cell surface or direct it to lysosomes for degradation. Can induce ubiquitination of LDLR leading to its subsequent degradation (PubMed:18799458, PubMed:17461796, PubMed:18197702, PubMed:22074827). Inhibits intracellular degradation of APOB via the autophagosome/lysosome pathway in a LDLR-independent manner. Involved in the disposal of non-acetylated intermediates of BACE1 in the early secretory pathway (PubMed:18660751). Inhibits epithelial Na(+) channel (ENaC)-mediated Na(+) absorption by reducing ENaC surface expression primarily by increasing its proteasomal degradation. Regulates neuronal apoptosis via modulation of LRP8/APOER2 levels and related anti-apoptotic signaling pathways",
                "Gene",
                "protein_coding",
                "1",
                1,
                55039447,
                55064852,
            ],
        ]
        self.assertListEqual(result_to_test, expected_result)

    def test_info_exon_expand(self):
        df = info("ENSTGUEE00000179311")
        # Drop NaN columns, since np.nan != np.nan
        result_to_test = df.dropna(axis=1).values.tolist()
        expected_result = [
            [
                "ENSTGUEE00000179311.1",
                "taeniopygia_guttata",
                "bTaeGut1_v1.p",
                [],
                "Exon",
                "1",
                -1,
                107526792,
                107526965,
            ]
        ]

        self.assertListEqual(result_to_test, expected_result)

    def test_info_bad_id(self):
        result = info(["banana"])
        self.assertIsNone(result, "Invalid ID output is not None.")
