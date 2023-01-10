import requests

ApiKey = ""

class nota:

    def __init__(self,numero,serie):
        self.numero = numero
        self.serie = serie
        url = f"https://bling.com.br/Api/v2/notafiscal/{self.numero}/{self.serie}/json/"
        payload = {"apikey": ApiKey}

        self.json = requests.get(url, params=payload).json()

        try: self.id = self.json['retorno']['notasfiscais'][0]['notafiscal']['id'] 
        except: self.id = "Sem informação"
        try: self.serie = self.json['retorno']['notasfiscais'][0]['notafiscal']['serie'] 
        except: self.serie = "Sem informação"
        try: self.numero = self.json['retorno']['notasfiscais'][0]['notafiscal']['numero'] 
        except: self.numero = "Sem informação"
        try: self.loja = self.json['retorno']['notasfiscais'][0]['notafiscal']['loja'] 
        except: self.loja = "Sem informação"
        try: self.numeroPedidoLoja = self.json['retorno']['notasfiscais'][0]['notafiscal']['numeroPedidoLoja'] 
        except: self.numeroPedidoLoja = "Sem informação"
        try: self.tipo = self.json['retorno']['notasfiscais'][0]['notafiscal']['tipo'] 
        except: self.tipo = "Sem informação"
        try: self.situacao = self.json['retorno']['notasfiscais'][0]['notafiscal']['situacao'] 
        except: self.situacao = "Sem informação"
        try: self.cliente = self.json['retorno']['notasfiscais'][0]['notafiscal']['cliente'] 
        except: self.cliente = "Sem informação"
        try: self.cliente_nome = self.json['retorno']['notasfiscais'][0]['notafiscal']['cliente']['nome'] 
        except: self.cliente_nome = "Sem informação"
        try: self.cliente_cnpj = self.json['retorno']['notasfiscais'][0]['notafiscal']['cliente']['cnpj'] 
        except: self.cliente_cnpj = "Sem informação"
        try: self.cliente_ie = self.json['retorno']['notasfiscais'][0]['notafiscal']['cliente']['ie'] 
        except: self.cliente_ie = "Sem informação"
        try: self.cliente_rg = self.json['retorno']['notasfiscais'][0]['notafiscal']['cliente']['rg'] 
        except: self.cliente_rg = "Sem informação"
        try: self.cliente_endereco = self.json['retorno']['notasfiscais'][0]['notafiscal']['cliente']['endereco'] 
        except: self.cliente_endereco = "Sem informação"
        try: self.cliente_numero = self.json['retorno']['notasfiscais'][0]['notafiscal']['cliente']['numero'] 
        except: self.cliente_numero = "Sem informação"
        try: self.cliente_complemento = self.json['retorno']['notasfiscais'][0]['notafiscal']['cliente']['complemento'] 
        except: self.cliente_complemento = "Sem informação"
        try: self.cliente_cidade = self.json['retorno']['notasfiscais'][0]['notafiscal']['cliente']['cidade'] 
        except: self.cliente_cidade = "Sem informação"
        try: self.cliente_bairro = self.json['retorno']['notasfiscais'][0]['notafiscal']['cliente']['bairro'] 
        except: self.cliente_bairro = "Sem informação"
        try: self.cliente_cep = self.json['retorno']['notasfiscais'][0]['notafiscal']['cliente']['cep'] 
        except: self.cliente_cep = "Sem informação"
        try: self.cliente_uf = self.json['retorno']['notasfiscais'][0]['notafiscal']['cliente']['uf'] 
        except: self.cliente_uf = "Sem informação"
        try: self.cliente_email = self.json['retorno']['notasfiscais'][0]['notafiscal']['cliente']['email'] 
        except: self.cliente_email = "Sem informação"
        try: self.cliente_fone = self.json['retorno']['notasfiscais'][0]['notafiscal']['cliente']['fone'] 
        except: self.cliente_fone = "Sem informação"
        try: self.contato = self.json['retorno']['notasfiscais'][0]['notafiscal']['contato'] 
        except: self.contato = "Sem informação"
        try: self.cnpj = self.json['retorno']['notasfiscais'][0]['notafiscal']['cnpj'] 
        except: self.cnpj = "Sem informação"
        try: self.vendedor = self.json['retorno']['notasfiscais'][0]['notafiscal']['vendedor'] 
        except: self.vendedor = "Sem informação"
        try: self.dataEmissao = self.json['retorno']['notasfiscais'][0]['notafiscal']['dataEmissao'] 
        except: self.dataEmissao = "Sem informação"
        try: self.valorNota = self.json['retorno']['notasfiscais'][0]['notafiscal']['valorNota'] 
        except: self.valorNota = "Sem informação"
        try: self.chaveAcesso = self.json['retorno']['notasfiscais'][0]['notafiscal']['chaveAcesso'] 
        except: self.chaveAcesso = "Sem informação"
        try: self.xml = self.json['retorno']['notasfiscais'][0]['notafiscal']['xml'] 
        except: self.xml = "Sem informação"
        try: self.linkDanfe = self.json['retorno']['notasfiscais'][0]['notafiscal']['linkDanfe'] 
        except: self.linkDanfe = "Sem informação"
        try: self.linkPDF = self.json['retorno']['notasfiscais'][0]['notafiscal']['linkPDF'] 
        except: self.linkPDF = "Sem informação"
        try: self.codigoRastreamento = self.json['retorno']['notasfiscais'][0]['notafiscal']['codigoRastreamento']['codigoRastreamento'] 
        except: self.codigoRastreamento = "Sem informação"
        try: self.cfops = self.json['retorno']['notasfiscais'][0]['notafiscal']['cfops'][0] 
        except: self.cfops = "Sem informação"
        try: self.tipoIntegracao = self.json['retorno']['notasfiscais'][0]['notafiscal']['tipoIntegracao'] 
        except: self.tipoIntegracao = "Sem informação"
        try: self.volume_id = self.json['retorno']['notasfiscais'][0]['notafiscal']['transporte']['volumes'][0]['volume']['id'][max] 
        except: self.volume_id = "Sem informação"
    
    class filtroPedido:

        def __init__(self,numero):
            url = f"https://bling.com.br/Api/v2/notasfiscais/json/"
            payload = {"filters": f"numeroPedidoLoja[{numero}]", "apikey": ApiKey}

            self.json = requests.get(url, params=payload).json()

            try: self.id = self.json['retorno']['notasfiscais'][0]['notafiscal']['id'] 
            except: self.id = "Sem informação"
            try: self.serie = self.json['retorno']['notasfiscais'][0]['notafiscal']['serie'] 
            except: self.serie = "Sem informação"
            try: self.numero = self.json['retorno']['notasfiscais'][0]['notafiscal']['numero'] 
            except: self.numero = "Sem informação"
            try: self.loja = self.json['retorno']['notasfiscais'][0]['notafiscal']['loja'] 
            except: self.loja = "Sem informação"
            try: self.numeroPedidoLoja = self.json['retorno']['notasfiscais'][0]['notafiscal']['numeroPedidoLoja'] 
            except: self.numeroPedidoLoja = "Sem informação"
            try: self.tipo = self.json['retorno']['notasfiscais'][0]['notafiscal']['tipo'] 
            except: self.tipo = "Sem informação"
            try: self.situacao = self.json['retorno']['notasfiscais'][0]['notafiscal']['situacao'] 
            except: self.situacao = "Sem informação"
            try: self.cliente = self.json['retorno']['notasfiscais'][0]['notafiscal']['cliente'] 
            except: self.cliente = "Sem informação"
            try: self.cliente_nome = self.json['retorno']['notasfiscais'][0]['notafiscal']['cliente']['nome'] 
            except: self.cliente_nome = "Sem informação"
            try: self.cliente_cnpj = self.json['retorno']['notasfiscais'][0]['notafiscal']['cliente']['cnpj'] 
            except: self.cliente_cnpj = "Sem informação"
            try: self.cliente_ie = self.json['retorno']['notasfiscais'][0]['notafiscal']['cliente']['ie'] 
            except: self.cliente_ie = "Sem informação"
            try: self.cliente_rg = self.json['retorno']['notasfiscais'][0]['notafiscal']['cliente']['rg'] 
            except: self.cliente_rg = "Sem informação"
            try: self.cliente_endereco = self.json['retorno']['notasfiscais'][0]['notafiscal']['cliente']['endereco'] 
            except: self.cliente_endereco = "Sem informação"
            try: self.cliente_numero = self.json['retorno']['notasfiscais'][0]['notafiscal']['cliente']['numero'] 
            except: self.cliente_numero = "Sem informação"
            try: self.cliente_complemento = self.json['retorno']['notasfiscais'][0]['notafiscal']['cliente']['complemento'] 
            except: self.cliente_complemento = "Sem informação"
            try: self.cliente_cidade = self.json['retorno']['notasfiscais'][0]['notafiscal']['cliente']['cidade'] 
            except: self.cliente_cidade = "Sem informação"
            try: self.cliente_bairro = self.json['retorno']['notasfiscais'][0]['notafiscal']['cliente']['bairro'] 
            except: self.cliente_bairro = "Sem informação"
            try: self.cliente_cep = self.json['retorno']['notasfiscais'][0]['notafiscal']['cliente']['cep'] 
            except: self.cliente_cep = "Sem informação"
            try: self.cliente_uf = self.json['retorno']['notasfiscais'][0]['notafiscal']['cliente']['uf'] 
            except: self.cliente_uf = "Sem informação"
            try: self.cliente_email = self.json['retorno']['notasfiscais'][0]['notafiscal']['cliente']['email'] 
            except: self.cliente_email = "Sem informação"
            try: self.cliente_fone = self.json['retorno']['notasfiscais'][0]['notafiscal']['cliente']['fone'] 
            except: self.cliente_fone = "Sem informação"
            try: self.contato = self.json['retorno']['notasfiscais'][0]['notafiscal']['contato'] 
            except: self.contato = "Sem informação"
            try: self.cnpj = self.json['retorno']['notasfiscais'][0]['notafiscal']['cnpj'] 
            except: self.cnpj = "Sem informação"
            try: self.vendedor = self.json['retorno']['notasfiscais'][0]['notafiscal']['vendedor'] 
            except: self.vendedor = "Sem informação"
            try: self.dataEmissao = self.json['retorno']['notasfiscais'][0]['notafiscal']['dataEmissao'] 
            except: self.dataEmissao = "Sem informação"
            try: self.valorNota = self.json['retorno']['notasfiscais'][0]['notafiscal']['valorNota'] 
            except: self.valorNota = "Sem informação"
            try: self.chaveAcesso = self.json['retorno']['notasfiscais'][0]['notafiscal']['chaveAcesso'] 
            except: self.chaveAcesso = "Sem informação"
            try: self.xml = self.json['retorno']['notasfiscais'][0]['notafiscal']['xml'] 
            except: self.xml = "Sem informação"
            try: self.linkDanfe = self.json['retorno']['notasfiscais'][0]['notafiscal']['linkDanfe'] 
            except: self.linkDanfe = "Sem informação"
            try: self.linkPDF = self.json['retorno']['notasfiscais'][0]['notafiscal']['linkPDF'] 
            except: self.linkPDF = "Sem informação"
            try: self.codigoRastreamento = self.json['retorno']['notasfiscais'][0]['notafiscal']['codigoRastreamento']['codigoRastreamento'] 
            except: self.codigoRastreamento = "Sem informação"
            try: self.cfops = self.json['retorno']['notasfiscais'][0]['notafiscal']['cfops'][0] 
            except: self.cfops = "Sem informação"
            try: self.tipoIntegracao = self.json['retorno']['notasfiscais'][0]['notafiscal']['tipoIntegracao'] 
            except: self.tipoIntegracao = "Sem informação"
            try: self.volume_id = self.json['retorno']['notasfiscais'][0]['notafiscal']['transporte']['volumes'][0]['volume']['id'][max] 
            except: self.volume_id = "Sem informação"

class pedidos:

    def __init__(self):
        url = f"https://bling.com.br/Api/v2/pedidos/page=1/json/"
        payload = {"apikey": ApiKey}

        #pedidos = requests.get(url, params=payload)
        #self.Tudo = pedidos.json()['retorno']['pedidos']

        self.json = requests.get(url, params=payload).json()
        self.pedidos = self.json['retorno']['pedidos']

        ind = 1
        while (len(self.json['retorno']['pedidos']) == 100):
            ind = ind + 1
            url = f"https://bling.com.br/Api/v2/pedidos/page={ind}/json/"

            self.json = requests.get(url, params=payload).json()
            self.pedidos = self.pedidos + self.json['retorno']['pedidos']

    def numero(self):
        numero = []
        for item in self.pedidos:
            try:
                numero.append(item['pedido']['numero'])
            except:
                numero.append("Sem informação")

        return numero

    def numeroPedidoLoja(self):
        numeroPedidoLoja = []
        for item in self.pedidos:
            try:
                numeroPedidoLoja.append(item['pedido']['numeroPedidoLoja'])
            except:
                numeroPedidoLoja.append("Sem informação")

        return numeroPedidoLoja

    def data(self):
        data = []
        for item in self.pedidos:
            try:
                data.append(item['pedido']['data'])
            except:
                data.append("Sem informação")

        return data

    class filtro_idSituacao:

        def __init__(self, valor):

            tabelaSit = """
            ID   ID_Herdado   Nome              Cor
            -------------------------------------------
            6    0            Em aberto         #E9DC40
            9    0            Atendido          #3FB57A
            12   0            Cancelado         #CBCBCB
            15   0            Em andamento      #0065F9
            18   0            Venda Agenciada   #FF7835
            21   0            Em digitação      #FF66E3
            24   0            Verificado        #85F39E
            """

            valores = ["6", "9", "12", "15", "18", "21", "24"]

            if valor in valores:
                url = f"https://bling.com.br/Api/v2/pedidos/page=1/json/"
                payload = {"apikey": ApiKey, "filters":f"idSituacao[{valor}]"}

                self.json = requests.get(url, params=payload).json()
                self.pedidos = self.json['retorno']['pedidos']

                ind = 1
                while (len(self.json['retorno']['pedidos']) == 100):
                    ind = ind + 1
                    url = f"https://bling.com.br/Api/v2/pedidos/page={ind}/json/"

                    self.json = requests.get(url, params=payload).json()
                    self.pedidos = self.pedidos + self.json['retorno']['pedidos']
            else:
                print("Situação incorreta, valores permitidos: " + tabelaSit)
                self.pedidos = []
                self.json = ""

        def numero(self):
            numero = []
            for item in self.pedidos:
                try:
                    numero.append(item['pedido']['numero'])
                except:
                    numero.append("Sem informação")

            return numero

        def numeroPedidoLoja(self):
            numeroPedidoLoja = []
            for item in self.pedidos:
                try:
                    numeroPedidoLoja.append(item['pedido']['numeroPedidoLoja'])
                except:
                    numeroPedidoLoja.append("Sem informação")

            return numeroPedidoLoja

        def data(self):
            data = []
            for item in self.pedidos:
                try:
                    data.append(item['pedido']['data'])
                except:
                    data.append("Sem informação")

            return data

class pedido:

    def __init__(self, numero):
        url = f"https://bling.com.br/Api/v2/pedido/{numero}/json/"
        payload = {"apikey": ApiKey}

        self.json = requests.get(url, params=payload).json()

        try: self.desconto = self.json['retorno']['pedidos'][0]['pedido']['desconto']
        except: self.desconto = "Sem informação"
        try: self.numeroPedidoLoja = self.json['retorno']['pedidos'][0]['pedido']['numeroPedidoLoja']
        except: self.numeroPedidoLoja = "Sem informação"
        try: self.data = self.json['retorno']['pedidos'][0]['pedido']['data']
        except: self.data = "Sem informação"

class produtos:

    def __init__(self, sku):
        url = f"https://bling.com.br/Api/v2/produto/{sku}/json/"
        payload = {"apikey": ApiKey}

        self.json = requests.get(url, params=payload).json()

class produto:

    def __init__(self, sku):
        url = f"https://bling.com.br/Api/v2/produto/{sku}/json/"
        payload = {"apikey": ApiKey, "imagem": "S"}

        #https://bling.com.br/Api/v2/produto/{sku}/json?apikey=keyyy&imagem=S

        self.json = requests.get(url, params=payload).json()

        try: self.imagens = self.json['retorno']['produtos'][0]['produto']['imagem']
        except: self.imagens = "Sem informação"
        try: self.sku = self.json['retorno']['produtos'][0]['produto']['codigo']
        except: self.sku = "Sem informação"
        try: self.titulo = self.json['retorno']['produtos'][0]['produto']['descricao']
        except: self.titulo = "Sem informação"
        try: self.condicao = self.json['retorno']['produtos'][0]['produto']['condicao']
        except: self.condicao = "Sem informação"
        try: self.marca = self.json['retorno']['produtos'][0]['produto']['marca']
        except: self.marca = "Sem informação"

    class atualizar:

        def __init__(self, sku, estoque):
            #xmll = '''<?xml version="1.0" encoding="UTF-8"?><produto><codigo>SW-A6-VM</codigo><descricao>SmartWatch A6 (Liso) Vermelhoaaaaa</descricao><estoque>10.00</estoque><deposito><id>14886556851</id><estoque>200</estoque></deposito>'''

            from xml.dom import minidom

            #cria documento
            doc = minidom.Document()

            #cria raiz e adicionar no documento
            raiz = doc.createElement('produto')
            doc.appendChild(raiz)

            #cria itens e adiciona na raiz
            #cod = doc.createElement('codigo')
            #desc = doc.createElement('descricao')
            esto = doc.createElement('estoque')
            #cod.appendChild(doc.createTextNode('SW-A6-VM'))
            #desc.appendChild(doc.createTextNode('SmartWatch A6 (Liso) VermelhoAAAAA'))
            esto.appendChild(doc.createTextNode(str(estoque)))
            #raiz.appendChild(cod)
            #raiz.appendChild(desc)
            raiz.appendChild(esto)

            #xmldoc = minidom.Document()
            print(raiz.toprettyxml())
            #print(doc)

            url = f"https://bling.com.br/Api/v2/produto/{sku}/json/"
            payload = {"apikey": ApiKey, "xml": raiz.toprettyxml()}
            #payload = {"apikey": ApiKey}

            self.json = requests.post(url, params=payload).json()

            try:
                self.json['retorno']['produtos'][0]['produto']['codigo']
            except:
                self.resultado = "erro"
            else:
                if self.json['retorno']['produtos'][0]['produto']['codigo'] == sku:
                    self.resultado = "sucesso"
                else:
                    self.resultado = "erro"

            #return self.json