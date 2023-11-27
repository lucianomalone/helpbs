import streamlit as st;


bar = st.sidebar

escolha = bar.selectbox('**Escolha um Assunto**',
                        ['','Facilidades','Linux','AWS','Select','Update'])

text = st.text('')

if text and escolha =='Facilidades':
    
    texto = str.upper(st.text_input('Converter em Maisculo', ''))
    t = st.write(texto)
    
    text = st.write('---')

    converte = st.text_input('Inverte Barra', '')
    nova =  converte.replace('\\','/')
    tconverte = st.write(nova)
    
    text = st.write('---')
   




if text and escolha =='Linux':
    text=st.write('**Criando Base no Servidor**')    
    text = st.text('database-restore -n')
    text = st.write('---')

    text=st.write('**Finalizando serviço Firebird**')    
    text = st.text('ps aux |grep firebird \nkill -9 + o PID do Processo')
    text = st.write('---')
     
    text=st.write('**Iniciando serviço Firebird**')    
    text = st.text('service firebird start \nservice firebird start')
    text = st.write('---')

    text=st.write('**Permissão no arquivo**')    
    text = st.text('chown firebird:firebird')
    text = st.write('---')

    text=st.write('**Colocar Base para gerar Backup**')    
    text = st.text('echo ThreeLions >> /opt/e-get/backup/backup.conf')
    
    text = st.write('---')

if text and escolha =='AWS':
    text=st.write('**Copiar do S3 para o Servidor aws**')    
    text = st.text('aws s3 cp CAMINHO COPIADO DA AWS .')
    
    text = st.write('---')

    text=st.write('**Copiar do servidor para o S3**')    
    text = st.text('aws s3 cp NOME DO ARQIVO  CAMINHO DA AWS ONDE SERA SALVO')
    text = st.write('---')

if text and escolha =='Select':
    text=st.write('**SELECT COLABORADOR**')    
    text = st.text('''
		select c.ID_COLABORADORES, p.NOME,u.LOGIN,c.IS_VENDEDOR,
from COLABORADORES c
inner join pessoas p
inner join USUARIOS u
on c.ID_PESSOA = p.ID_PESSOA
on p.ID_PESSOA = u.ID_PESSOA
where c.ID_COLABORADORES=19
	''')
    text = st.write('---')

    text=st.write('**SELECT consulta cliente vincula integração**')    
    text = st.text('''
		select c.ID_CLIENTE,p.NOME,p.APELIDO, i.ID_CLIENTE, i.DATE_UPDATE,i.COD_INTEGRADO
from  clientes c
inner join INTEGRACAO_CLIENTE i
inner join PESSOAS p
on p.ID_PESSOA = c.ID_PESSOA
on c.ID_CLIENTE = i.ID_CLIENTE
	''')
    text = st.write('---')


    text=st.write('**SELECT equipamentos Duplicados**')    
    text = st.text('''
		SELECT e.patrimonio, Count(*) FROM equipamentos e
GROUP BY e.patrimonio
HAVING Count(*) > 1
	''')
    text = st.write('---')

    text=st.write('**SELECT Pedidos Deletados**')    
    text = st.text('''
		SELECT
 o.N_PEDIDO as Numero_Pedido,
 o.VALOR_PEDIDO,
 p.nome as Nome_Cliente,
 c.ID_CLIENTE,
 o.DATE_CAD as Data_Criacao,
 o.CAD_USER as User_Q_Criou,
 o.CAD_USER,
 o.DELETED as Deletado,
 o.DATE_UPDATE as Data_Exclusao,
 o.DEL_USER,
 u.LOGIN
from  ORDENS_VENDA o
inner join CLIENTES c on c.ID_CLIENTE = o.ID_CLIENTE
inner join PESSOAS p on p.ID_PESSOA = c.ID_PESSOA
inner join USUARIOS u on u.ID_USUARIO = o.DEL_USER
WHERE o.DELETED=1  and o.DATE_CAD >= '01.10.2020' and o.DATE_CAD<='29.10.2023'
	''')
    text = st.write('---')
  




if text and escolha =='Update':
     text=st.write('**Alterar dias de visita**')    
     text = st.text('''
               =SE(B2="Segunda - Feira";0;SE(B2="Terça - Feira";1;SE(B2="Quarta - Feira";2;SE(B2="Quinta - Feira";3;SE(B2="Sexta - Feira";4;SE(B2="Sabado";5;SE(B2="Domingo";6)))))))
            ''')
     text = st.write('---')