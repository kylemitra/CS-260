COMPSCI 260 - Problem Set 4, Problem 4
Due: Fri 25 Oct 2019, 5pm

Name: Kyle Mitra
NetID: km423

Statement of collaboration and resources used (put None if you worked
entirely without collaboration or resources; otherwise cite carefully): Office Hours

My solutions and comments for this problem are below.
-----------------------------------------------------
a) See Code

b) The up-most optimal local alignment is:
  LGSGQSANLGASCSGSGYEVLSAYALPPPPMASSSAADSSFSAASSASANVTPHHTIAQESCPSPCSSASHFGVAHSSGFSSDPISPAVSSYAHMSYNYASSANTMTPSSASGTSAHVAPGKQQFFASCFYSPWV 
 SSSFSTSVYQPIPQPTTPVSSFTSGSMLGRTDTALTNTYSALPPMPSFTMANNLPMQPPVPSQTSSYSCMLPTSPSVNGRSYDTYTPPHMQTHMNSQPMGTSGTTSTGLISPGVSVPVQVPGSEPDMSQYWPRLQ

The down-most optimal local alignment is:
 LGSGQSANLGASCSGSGYEVLSAYALPPPPMASSSAADSSFSAASSASANVTPHHTIAQESCPSPCSSASHFGVAHSSGFSSDPISPAVSSYAHMSYNYASSANTMTPSSASGTSAHVAPGKQQFFASCFYSPWV 
 SSSFSTSVYQPIPQPTTPVSSFTSGSMLGRTDTALTNTYSALPPMPSFTMANNLPMQPPVPSQTSSYSCMLPTSPSVNGRSYDTYTPPHMQTHMNSQPMGTSGTTSTGLISPGVSVPVQVPGSEPDMSQYWPRLQ

c) The values of V'(m,n) are the optimal score of any suffix of the mth prefix of X aligned to any suffix of the nth prefix of Y. All the scores of V' are non-negative and less than or equal to the best local alignment unless V'(m'n) is equal to the maximum score of the entire table. 

d) P63015 is the protein PAX6_MOUSE. It is a transcription factor with important functions in the development of the eye, nose, central nervous system, and pancreas. O18381 is the protein PAX6_DROME. This protein is involved in eye morphogenesis of the fruit fly. Both of these are Paired box proteins (Pax-6) and play a role in the development of the eyes in their respective organisms. In this context, the local alignment results would be the regions of each protein which influence the development of the eye, eye morphogenesis to be specific, for each respective organism. 




