import requests

ApiKey = ""

class nota:

    def __init__(self,numero,serie):
        self.numero = numero
        self.serie = serie
        url = f"https://bling.com.br/Api/v2/notafiscal/{self.numero}/{self.serie}/json/"
        payload = {"apikey": ApiKey}

        self.json = requests.get(url, params=payload).json()

        self.id = self.json['retorno']['notasfiscais'][0]['notafiscal']['id']
        self.serie = self.json['retorno']['notasfiscais'][0]['notafiscal']['serie']
        self.numero = self.json['retorno']['notasfiscais'][0]['notafiscal']['numero']
        self.loja = self.json['retorno']['notasfiscais'][0]['notafiscal']['loja']
        self.numeroPedidoLoja = self.json['retorno']['notasfiscais'][0]['notafiscal']['numeroPedidoLoja']
        self.tipo = self.json['retorno']['notasfiscais'][0]['notafiscal']['tipo']
        self.situacao = self.json['retorno']['notasfiscais'][0]['notafiscal']['situacao']
        self.cliente = self.json['retorno']['notasfiscais'][0]['notafiscal']['cliente']
        self.cliente_nome = self.json['retorno']['notasfiscais'][0]['notafiscal']['cliente']['nome']
        self.cliente_cnpj = self.json['retorno']['notasfiscais'][0]['notafiscal']['cliente']['cnpj']
        self.cliente_ie = self.json['retorno']['notasfiscais'][0]['notafiscal']['cliente']['ie']
        self.cliente_rg = self.json['retorno']['notasfiscais'][0]['notafiscal']['cliente']['rg']
        self.cliente_endereco = self.json['retorno']['notasfiscais'][0]['notafiscal']['cliente']['endereco']
        self.cliente_numero = self.json['retorno']['notasfiscais'][0]['notafiscal']['cliente']['numero']
        self.cliente_complemento = self.json['retorno']['notasfiscais'][0]['notafiscal']['cliente']['complemento']
        self.cliente_cidade = self.json['retorno']['notasfiscais'][0]['notafiscal']['cliente']['cidade']
        self.cliente_bairro = self.json['retorno']['notasfiscais'][0]['notafiscal']['cliente']['bairro']
        self.cliente_cep = self.json['retorno']['notasfiscais'][0]['notafiscal']['cliente']['cep']
        self.cliente_uf = self.json['retorno']['notasfiscais'][0]['notafiscal']['cliente']['uf']
        self.cliente_email = self.json['retorno']['notasfiscais'][0]['notafiscal']['cliente']['email']
        self.cliente_fone = self.json['retorno']['notasfiscais'][0]['notafiscal']['cliente']['fone']
        self.contato = self.json['retorno']['notasfiscais'][0]['notafiscal']['contato']
        self.cnpj = self.json['retorno']['notasfiscais'][0]['notafiscal']['cnpj']
        self.vendedor = self.json['retorno']['notasfiscais'][0]['notafiscal']['vendedor']
        self.dataEmissao = self.json['retorno']['notasfiscais'][0]['notafiscal']['dataEmissao']
        self.valorNota = self.json['retorno']['notasfiscais'][0]['notafiscal']['valorNota']
        self.chaveAcesso = self.json['retorno']['notasfiscais'][0]['notafiscal']['chaveAcesso']
        self.xml = self.json['retorno']['notasfiscais'][0]['notafiscal']['xml']
        self.linkDanfe = self.json['retorno']['notasfiscais'][0]['notafiscal']['linkDanfe']
        self.linkPDF = self.json['retorno']['notasfiscais'][0]['notafiscal']['linkPDF']
        self.codigoRastreamento = self.json['retorno']['notasfiscais'][0]['notafiscal']['codigoRastreamento']['codigoRastreamento']
        self.cfops = self.json['retorno']['notasfiscais'][0]['notafiscal']['cfops'][0]
        self.tipoIntegracao = self.json['retorno']['notasfiscais'][0]['notafiscal']['tipoIntegracao']
        self.volume_id = self.json['retorno']['notasfiscais'][0]['notafiscal']['transporte']['volumes'][0]['volume']['id'][max]
    
    class filtroPedido:

        def __init__(self,numero):
            url = f"https://bling.com.br/Api/v2/notasfiscais/json/"
            payload = {"filters": f"numeroPedidoLoja[{numero}]", "apikey": ApiKey}

            self.json = requests.get(url, params=payload).json()

            self.id = self.json['retorno']['notasfiscais'][0]['notafiscal']['id']
            self.serie = self.json['retorno']['notasfiscais'][0]['notafiscal']['serie']
            self.numero = self.json['retorno']['notasfiscais'][0]['notafiscal']['numero']
            self.loja = self.json['retorno']['notasfiscais'][0]['notafiscal']['loja']
            self.numeroPedidoLoja = self.json['retorno']['notasfiscais'][0]['notafiscal']['numeroPedidoLoja']
            self.tipo = self.json['retorno']['notasfiscais'][0]['notafiscal']['tipo']
            self.situacao = self.json['retorno']['notasfiscais'][0]['notafiscal']['situacao']
            self.cliente = self.json['retorno']['notasfiscais'][0]['notafiscal']['cliente']
            self.cliente_nome = self.json['retorno']['notasfiscais'][0]['notafiscal']['cliente']['nome']
            self.cliente_cnpj = self.json['retorno']['notasfiscais'][0]['notafiscal']['cliente']['cnpj']
            self.cliente_ie = self.json['retorno']['notasfiscais'][0]['notafiscal']['cliente']['ie']
            self.cliente_rg = self.json['retorno']['notasfiscais'][0]['notafiscal']['cliente']['rg']
            self.cliente_endereco = self.json['retorno']['notasfiscais'][0]['notafiscal']['cliente']['endereco']
            self.cliente_numero = self.json['retorno']['notasfiscais'][0]['notafiscal']['cliente']['numero']
            self.cliente_complemento = self.json['retorno']['notasfiscais'][0]['notafiscal']['cliente']['complemento']
            self.cliente_cidade = self.json['retorno']['notasfiscais'][0]['notafiscal']['cliente']['cidade']
            self.cliente_bairro = self.json['retorno']['notasfiscais'][0]['notafiscal']['cliente']['bairro']
            self.cliente_cep = self.json['retorno']['notasfiscais'][0]['notafiscal']['cliente']['cep']
            self.cliente_uf = self.json['retorno']['notasfiscais'][0]['notafiscal']['cliente']['uf']
            self.cliente_email = self.json['retorno']['notasfiscais'][0]['notafiscal']['cliente']['email']
            self.cliente_fone = self.json['retorno']['notasfiscais'][0]['notafiscal']['cliente']['fone']
            self.contato = self.json['retorno']['notasfiscais'][0]['notafiscal']['contato']
            self.cnpj = self.json['retorno']['notasfiscais'][0]['notafiscal']['cnpj']
            self.vendedor = self.json['retorno']['notasfiscais'][0]['notafiscal']['vendedor']
            self.dataEmissao = self.json['retorno']['notasfiscais'][0]['notafiscal']['dataEmissao']
            self.valorNota = self.json['retorno']['notasfiscais'][0]['notafiscal']['valorNota']
            self.chaveAcesso = self.json['retorno']['notasfiscais'][0]['notafiscal']['chaveAcesso']
            self.xml = self.json['retorno']['notasfiscais'][0]['notafiscal']['xml']
            self.linkDanfe = self.json['retorno']['notasfiscais'][0]['notafiscal']['linkDanfe']
            self.linkPDF = self.json['retorno']['notasfiscais'][0]['notafiscal']['linkPDF']
            self.codigoRastreamento = self.json['retorno']['notasfiscais'][0]['notafiscal']['codigoRastreamento']['codigoRastreamento']
            self.cfops = self.json['retorno']['notasfiscais'][0]['notafiscal']['cfops'][0]
            self.tipoIntegracao = self.json['retorno']['notasfiscais'][0]['notafiscal']['tipoIntegracao']
            self.volume_id = self.json['retorno']['notasfiscais'][0]['notafiscal']['transporte']['volumes'][0]['volume']['id'][max]

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

        self.desconto = self.json['retorno']['pedidos'][0]['pedido']['desconto']
        self.numeroPedidoLoja = self.json['retorno']['pedidos'][0]['pedido']['numeroPedidoLoja']
        self.data = self.json['retorno']['pedidos'][0]['pedido']['data']

class produtos:

    def __init__(self, sku):
        url = f"https://bling.com.br/Api/v2/produto/{sku}/json/"
        payload = {"apikey": ApiKey}

        self.json = requests.get(url, params=payload).json()

class produto(object):

    def __init__(self, sku):
        url = f"https://bling.com.br/Api/v2/produto/{sku}/json/"
        payload = {"apikey": ApiKey, "imagem": "S"}

        #https://bling.com.br/Api/v2/produto/{sku}/json?apikey=keyyy&imagem=S

        self.json = requests.get(url, params=payload).json()

        self.imagens = self.json['retorno']['produtos'][0]['produto']['imagem']
        self.sku = self.json['retorno']['produtos'][0]['produto']['codigo']
        self.titulo = self.json['retorno']['produtos'][0]['produto']['descricao']
        self.condicao = self.json['retorno']['produtos'][0]['produto']['condicao']
        self.marca = self.json['retorno']['produtos'][0]['produto']['marca']