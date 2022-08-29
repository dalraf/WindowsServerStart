conteudo = '''
# copyright (c) 1993-2009 microsoft corp.
#
# this is a sample hosts file used by microsoft tcp/ip for windows.
#
# this file contains the mappings of ip addresses to host names. each
# entry should be kept on an individual line. the ip address should
# be placed in the first column followed by the corresponding host name.
# the ip address and the host name should be separated by at least one
# space.
#
# additionally, comments (such as these) may be inserted on individual
# lines or following the machine name denoted by a '#' symbol.
#
# for example:
#
#      102.54.94.97     rhino.acme.com          # source server
#       38.25.63.10     x.acme.com              # x client host
# localhost name resolution is handled within dns itself.
#	127.0.0.1       localhost
#	::1             localhost


172.16.2.147	atelegado.sisbr.coop.br  
172.16.1.139	portal.sisbr.coop.br 
172.16.0.170	atendimento.sisbr.coop.br 
172.16.0.74     atendimentochat.sisbr.coop.br 
172.16.0.19     pldpcf.sisbr.coop.br 
172.16.0.206	boctb.sisbr.coop.br 
172.16.0.207	riscolimite.sisbr.coop.br 
172.16.0.208	rds.sisbr.coop.br 
172.16.0.74     intranet.sicoob.com.br 
172.16.0.5      cregeo.sisbr.coop.br 
172.16.0.5      sins.sisbr.coop.br 
172.16.0.99     sms.sisbr.coop.br 
172.16.0.3      cdp.geotrust.com 
172.16.0.177	bocompe.sisbr.coop.br 
172.16.0.168	convenios.sisbr.coop.br 
172.16.1.201	sgm.sisbr.coop.br 
172.16.0.50     seguros.sisbr.coop.br 
172.16.1.142	intranet.sicoob.com.br 
172.16.0.67     atendimento.sicoob.com.br 
172.16.1.65     sisbranalitico.sisbr.coop.br 
172.16.2.98     bocnv.sisbr.coop.br
172.16.2.66     consorcio.sisbr.com.br
172.16.0.56     bocredito.sisbr.coop.br
172.16.0.210    hsqlprod1.sisbr.coop.br
172.16.0.209    portalrh.sisbr.coop.br
172.16.0.7      pticluster.sisbr.coop.br
172.16.0.101    sofc.sisbr.coop.br
172.16.2.66     consorcio.sisbr.com.br
172.16.2.13     sistemas.sisbr.com.br
10.250.1.19     icl.cecremge.org.br
10.250.1.19     promocaofacaparte.cecremge.org
10.250.1.19     contasdigitais.cecremge.org
'''
hosts_file = 'c:\\Windows\\system32\\drivers\\etc\\hosts'
with open(hosts_file, 'w') as hostfile:
    hostfile.write(conteudo)
