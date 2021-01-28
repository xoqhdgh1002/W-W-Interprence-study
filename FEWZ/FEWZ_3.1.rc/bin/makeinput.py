import sys

wp_mass = sys.argv[1]
mode = sys.argv[2]
order = sys.argv[3]
pdfset = sys.argv[4]
input_name = sys.argv[5]

w_mass = 80.403
w_width = 2.141

wp_width = (4.0/3.0)*(int(wp_mass)/w_mass)*w_width
wp_width_lv = wp_width/12.0
wp_width = str(wp_width)
wp_width_lv = str(wp_width_lv)

input_txt="""=============================================
'CMS collision energy (GeV)    = ' 14000d0
=============================================
'Factorization scale  (GeV)    = ' """+wp_mass+"""d0
'Renormalization scale  (GeV)  = ' """+wp_mass+"""d0
=============================================
'W production (1=pp W-, 2=ppbar W-, 3=pp W+, 4=ppbar W+) = ' """+mode+"""
=============================================
'Alpha QED                     = ' 0.0078125d0
'Fermi constant (1/GeV^2)      = ' 0.0000116637d0
=============================================
'W mass (GeV)                  = ' """+wp_mass+"""d0
'W width (GeV)                 = ' """+wp_width+"""d0
'W->lv partial width           = ' """+wp_width_lv+"""d0
'sin^2(theta)                  = ' 0.22255d0
CKM matrix elements (not squared)
'Vud                           = ' 0.97428d0
'Vus=Vcd                       = ' 0.2253d0
'Vcs                           = ' 0.97345d0
'Vub                           = ' 0.00347d0
'Vcb                           = ' 0.041d0
=============================================
Vegas Parameters
'Relative accuracy (in %)           = ' 0d0
'Absolute accuracy                  = ' 0d0
'Number of calls per iteration      = ' 1000000
'Number of increase calls per iter. = ' 500000
'Maximum number of evaluations      = ' 200000000
'Random number seed for Vegas       = ' 111
=============================================
'QCD Perturb. Order (0=LO, 1=NLO, 2=NNLO) = ' """+order+"""
'W pole focus (1=Yes, 0=No)     = ' 1
=============================================
'Lepton-pair invariant mass minimum = ' 0d0
'Lepton-pair invariant mass maximum = ' 14000d0
'Transverse mass minimum            = ' 0d0
'Transverse mass maximum            = ' 14000d0
'W pT minimum                       = ' 0d0
'W pT maximum                       = ' 14000d0
'W rapidity minimum                 = ' -20d0
'W rapidity maximum                 = ' 20d0
'Charged lepton pT minimum          = ' 0d0
'Charged lepton pT maximum          = ' 14000d0
'Missing pT minimum                 = ' 0d0
'Missing pT maximum                 = ' 14000d0
'pT min for softer lepton           = ' 0d0
'pT max for softer lepton           = ' 7000d0
'pT min for harder lepton           = ' 0d0
'pT max for harder lepton           = ' 7000d0
Taking absolute value of lepton pseudorapidity?
'(yes = 1, no = 0)                  = ' 1
'Ch. lepton pseudorapidity minimum  = ' 0d0
'Ch. lepton pseudorapidity maximum  = ' 100d0
JET DEFINITION-------------------------------
Jet Algorithm & Cone Size ('ktal'=kT algorithm, 'aktal'=anti-kT algorithm, 'cone'=cone)
'ktal, aktal or cone                = ' ktal
'Jet algorithm cone size (deltaR)   = ' 0.4d0
'DeltaR separation for cone algo    = ' 1.3
'Minimum pT for observable jets     = ' 20d0
'Maximum eta for observable jets    = ' 4.5d0
JET CUTS--------------------------------------
'Minimum Number of Jets             = ' 0
'Maximum Number of Jets             = ' 2
'Min. leading jet pT                = ' 0d0
ISOLATION CUTS-------------------------------
'Lep-missing deltaPhi min           = ' 0.0d0
'Lep-missing deltaPhi max           = ' 4.0d0
'Lep-Jet deltaR minimum             = ' 0.0d0
=============================================
(See manual for complete listing)
'PDF set =                        ' '"""+pdfset+"""'
'Turn off PDF error (1=Yes, 0=No)    = ' 1
(Active for MSTW2008 only, if PDF error is on:)
(Compute PDF+as errors: 1; just PDF errors: 0)
'Which alphaS                       = ' 0
(Active for MSTW2008 only; 0: 90 CL for PDFs+alphas, 1: 68 CL)
'PDF+alphas confidence level        = ' 1
=============================================
"""

inputfile = open(input_name,"w")
inputfile.write(input_txt)
inputfile.close()


