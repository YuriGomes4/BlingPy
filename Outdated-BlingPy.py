from ast import arg
#from asyncio.windows_events import NULL
from certifi import where
import requests

KeyApi = ""

def ApiKey(keyy):
    global KeyApi
    KeyApi = keyy

class notasFiltroPedido(object):

    def __init__(self,numero):
        #self.num = num
        #self.serie = serie
        url = f"https://bling.com.br/Api/v2/notasfiscais/json/"
        payload = {"filters": f"numeroPedidoLoja[{numero}]", "apikey": KeyApi}

        self.nota = requests.get(url, params=payload)
        #print(self.nota.json())

    def id(self):
        return self.nota.json()['retorno']['notasfiscais'][0]['notafiscal']['id']
    def serie(self):
        return self.nota.json()['retorno']['notasfiscais'][0]['notafiscal']['serie']
    def numero(self):
        return self.nota.json()['retorno']['notasfiscais'][0]['notafiscal']['numero']
    def loja(self):
        return self.nota.json()['retorno']['notasfiscais'][0]['notafiscal']['loja']
    def numeroPedidoLoja(self):
        return self.nota.json()['retorno']['notasfiscais'][0]['notafiscal']['numeroPedidoLoja']
    def tipo(self):
        return self.nota.json()['retorno']['notasfiscais'][0]['notafiscal']['tipo']
    def situacao(self):
        return self.nota.json()['retorno']['notasfiscais'][0]['notafiscal']['situacao']
    def cliente(self):
        return self.nota.json()['retorno']['notasfiscais'][0]['notafiscal']['cliente']
    def cliente_nome(self):
        return self.nota.json()['retorno']['notasfiscais'][0]['notafiscal']['cliente']['nome']
    def cliente_cnpj(self):
        return self.nota.json()['retorno']['notasfiscais'][0]['notafiscal']['cliente']['cnpj']
    def cliente_ie(self):
        return self.nota.json()['retorno']['notasfiscais'][0]['notafiscal']['cliente']['ie']
    def cliente_rg(self):
        return self.nota.json()['retorno']['notasfiscais'][0]['notafiscal']['cliente']['rg']
    def cliente_endereco(self):
        return self.nota.json()['retorno']['notasfiscais'][0]['notafiscal']['cliente']['endereco']
    def cliente_numero(self):
        return self.nota.json()['retorno']['notasfiscais'][0]['notafiscal']['cliente']['numero']
    def cliente_complemento(self):
        return self.nota.json()['retorno']['notasfiscais'][0]['notafiscal']['cliente']['complemento']
    def cliente_cidade(self):
        return self.nota.json()['retorno']['notasfiscais'][0]['notafiscal']['cliente']['cidade']
    def cliente_bairro(self):
        return self.nota.json()['retorno']['notasfiscais'][0]['notafiscal']['cliente']['bairro']
    def cliente_cep(self):
        return self.nota.json()['retorno']['notasfiscais'][0]['notafiscal']['cliente']['cep']
    def cliente_uf(self):
        return self.nota.json()['retorno']['notasfiscais'][0]['notafiscal']['cliente']['uf']
    def cliente_email(self):
        return self.nota.json()['retorno']['notasfiscais'][0]['notafiscal']['cliente']['email']
    def cliente_fone(self):
        return self.nota.json()['retorno']['notasfiscais'][0]['notafiscal']['cliente']['fone']
    def contato(self):
        return self.nota.json()['retorno']['notasfiscais'][0]['notafiscal']['contato']
    def cnpj(self):
        return self.nota.json()['retorno']['notasfiscais'][0]['notafiscal']['cnpj']
    def vendedor(self):
        return self.nota.json()['retorno']['notasfiscais'][0]['notafiscal']['vendedor']
    def dataEmissao(self):
        return self.nota.json()['retorno']['notasfiscais'][0]['notafiscal']['dataEmissao']
    def valorNota(self):
        return self.nota.json()['retorno']['notasfiscais'][0]['notafiscal']['valorNota']
    def chaveAcesso(self):
        return self.nota.json()['retorno']['notasfiscais'][0]['notafiscal']['chaveAcesso']
    def xml(self):
        return self.nota.json()['retorno']['notasfiscais'][0]['notafiscal']['xml']
    def linkDanfe(self):
        return self.nota.json()['retorno']['notasfiscais'][0]['notafiscal']['linkDanfe']
    def linkPDF(self):
        return self.nota.json()['retorno']['notasfiscais'][0]['notafiscal']['linkPDF']
    def codigoRastreamento(self):
        return self.nota.json()['retorno']['notasfiscais'][0]['notafiscal']['codigoRastreamento']['codigoRastreamento']
    def cfops(self):
        return self.nota.json()['retorno']['notasfiscais'][0]['notafiscal']['cfops'][0]
    def tipoIntegracao(self):
        return self.nota.json()['retorno']['notasfiscais'][0]['notafiscal']['tipoIntegracao']
    def volume_id(self,):
        return self.nota.json()['retorno']['notasfiscais'][0]['notafiscal']['transporte']['volumes'][0]['volume']['id'][max]

    def json(self):
        print(self.nota.content)

    def teste2(self):
        return self.nota.json()['retorno']['notasfiscais'][0]['notafiscal']['numero']

class nota(object):

    #nota = NULL

    def __init__(self,numero,serie):
        self.numero = numero
        self.serie = serie
        url = f"https://bling.com.br/Api/v2/notafiscal/{self.numero}/{self.serie}/json/"
        payload = {"apikey": KeyApi}

        self.nota = requests.get(url, params=payload)

    #region - Atributos nota

    def id(self):
        return self.nota.json()['retorno']['notasfiscais'][0]['notafiscal']['id']
    def serie(self):
        return self.nota.json()['retorno']['notasfiscais'][0]['notafiscal']['serie']
    def numero(self):
        return self.nota.json()['retorno']['notasfiscais'][0]['notafiscal']['numero']
    def loja(self):
        return self.nota.json()['retorno']['notasfiscais'][0]['notafiscal']['loja']
    def numeroPedidoLoja(self):
        return self.nota.json()['retorno']['notasfiscais'][0]['notafiscal']['numeroPedidoLoja']
    def tipo(self):
        return self.nota.json()['retorno']['notasfiscais'][0]['notafiscal']['tipo']
    def situacao(self):
        return self.nota.json()['retorno']['notasfiscais'][0]['notafiscal']['situacao']
    def cliente(self):
        return self.nota.json()['retorno']['notasfiscais'][0]['notafiscal']['cliente']
    def cliente_nome(self):
        return self.nota.json()['retorno']['notasfiscais'][0]['notafiscal']['cliente']['nome']
    def cliente_cnpj(self):
        return self.nota.json()['retorno']['notasfiscais'][0]['notafiscal']['cliente']['cnpj']
    def cliente_ie(self):
        return self.nota.json()['retorno']['notasfiscais'][0]['notafiscal']['cliente']['ie']
    def cliente_rg(self):
        return self.nota.json()['retorno']['notasfiscais'][0]['notafiscal']['cliente']['rg']
    def cliente_endereco(self):
        return self.nota.json()['retorno']['notasfiscais'][0]['notafiscal']['cliente']['endereco']
    def cliente_numero(self):
        return self.nota.json()['retorno']['notasfiscais'][0]['notafiscal']['cliente']['numero']
    def cliente_complemento(self):
        return self.nota.json()['retorno']['notasfiscais'][0]['notafiscal']['cliente']['complemento']
    def cliente_cidade(self):
        return self.nota.json()['retorno']['notasfiscais'][0]['notafiscal']['cliente']['cidade']
    def cliente_bairro(self):
        return self.nota.json()['retorno']['notasfiscais'][0]['notafiscal']['cliente']['bairro']
    def cliente_cep(self):
        return self.nota.json()['retorno']['notasfiscais'][0]['notafiscal']['cliente']['cep']
    def cliente_uf(self):
        return self.nota.json()['retorno']['notasfiscais'][0]['notafiscal']['cliente']['uf']
    def cliente_email(self):
        return self.nota.json()['retorno']['notasfiscais'][0]['notafiscal']['cliente']['email']
    def cliente_fone(self):
        return self.nota.json()['retorno']['notasfiscais'][0]['notafiscal']['cliente']['fone']
    def contato(self):
        return self.nota.json()['retorno']['notasfiscais'][0]['notafiscal']['contato']
    def cnpj(self):
        return self.nota.json()['retorno']['notasfiscais'][0]['notafiscal']['cnpj']
    def vendedor(self):
        return self.nota.json()['retorno']['notasfiscais'][0]['notafiscal']['vendedor']
    def dataEmissao(self):
        return self.nota.json()['retorno']['notasfiscais'][0]['notafiscal']['dataEmissao']
    def valorNota(self):
        return self.nota.json()['retorno']['notasfiscais'][0]['notafiscal']['valorNota']
    def chaveAcesso(self):
        return self.nota.json()['retorno']['notasfiscais'][0]['notafiscal']['chaveAcesso']
    def xml(self):
        return self.nota.json()['retorno']['notasfiscais'][0]['notafiscal']['xml']
    def linkDanfe(self):
        return self.nota.json()['retorno']['notasfiscais'][0]['notafiscal']['linkDanfe']
    def linkPDF(self):
        return self.nota.json()['retorno']['notasfiscais'][0]['notafiscal']['linkPDF']
    def codigoRastreamento(self):
        return self.nota.json()['retorno']['notasfiscais'][0]['notafiscal']['codigoRastreamento']['codigoRastreamento']
    def cfops(self):
        return self.nota.json()['retorno']['notasfiscais'][0]['notafiscal']['cfops'][0]
    def tipoIntegracao(self):
        return self.nota.json()['retorno']['notasfiscais'][0]['notafiscal']['tipoIntegracao']
    def volume_id(self,):
        return self.nota.json()['retorno']['notasfiscais'][0]['notafiscal']['transporte']['volumes'][0]['volume']['id'][max]

    #endregion

    def json(self):
        return self.nota.content

class pedidos(object):

    #Tudo = NULL

    def __init__(self, filtro="none", valor="0"):
        print(filtro)
        url = f"https://bling.com.br/Api/v2/pedidos/page=1/json/"
        if filtro == "situacao":
            payload = {"apikey": KeyApi, "filters":f"idSituacao[{valor}]"}
        else:
            payload = {"apikey": KeyApi}

        pedidos = requests.get(url, params=payload)

        #global Tudo
        self.Tudo = pedidos.json()['retorno']['pedidos']

        ind = 1
        while (len(pedidos.json()['retorno']['pedidos']) == 100):
            ind = ind + 1
            url = f"https://bling.com.br/Api/v2/pedidos/page={ind}/json/"

            pedidos = requests.get(url, params=payload)
            self.Tudo = self.Tudo + pedidos.json()['retorno']['pedidos']

    def numero(self):
        numero = []
        for item in self.Tudo:
            numero.append(item['pedido']['numero'])

        return numero

    def numeroPedidoLoja(self):
        numeroPedidoLoja = []
        for item in self.Tudo:
            try:
                numeroPedidoLoja.append(item['pedido']['numeroPedidoLoja'])
            except:
                numeroPedidoLoja.append("Sem número")

        return numeroPedidoLoja

    def data(self):
        #global Tudo
        #self.Tudo
        data = []
        for item in self.Tudo:
            data.append(item['pedido']['data'])

        return data

    def json(self):
        #global Tudo
        return self.Tudo

    def pagina(self, pag):
        print(str(pag))
        url = f"https://bling.com.br/Api/v2/pedidos/page={str(pag)}/json/"
        payload = {"apikey": KeyApi}

        pedidos = requests.get(url, params=payload)

        #global Tudo
        Tudo = pedidos.json()['retorno']['pedidos']

        return Tudo

    def situacao(self, situacao):
        url = f"https://bling.com.br/Api/v2/pedidos/page=1/json/"
        payload = {"apikey": KeyApi, "filters":f"idSituacao[{situacao}]"}

        self.pedidos = requests.get(url, params=payload)

        #global Tudo
        self.Tudo = self.pedidos.json()['retorno']['pedidos']

        ind = 1
        while (len(self.pedidos.json()['retorno']['pedidos']) == 100):
            ind = ind + 1
            url = f"https://bling.com.br/Api/v2/pedidos/page={ind}/json/"

            self.pedidos = requests.get(url, params=payload)
            self.Tudo = self.Tudo + self.pedidos.json()['retorno']['pedidos']

        return self.Tudo

class pedido(object):

    def __init__(self, numero):
        self.numero = numero
        url = f"https://bling.com.br/Api/v2/pedido/{self.numero}/json/"
        payload = {"apikey": KeyApi}

        self.pedido = requests.get(url, params=payload)

    def desconto(self):
        return self.pedido.json()['retorno']['pedidos'][0]['pedido']['desconto']

    def numeroPedidoLoja(self):
        return self.pedido.json()['retorno']['pedidos'][0]['pedido']['numeroPedidoLoja']

    def data(self):
        return self.pedido.json()['retorno']['pedidos'][0]['pedido']['data']

    def json(self):
        return self.pedido.json()

class produtos(object):

    #All = NULL

    def __init__(self):
        url = f"https://bling.com.br/Api/v2/produto/DS4-ORANGE/json/"
        payload = {"apikey": KeyApi}

        self.produtos = requests.get(url, params=payload)

        global All
        All = self.produtos.json()['retorno']['produtos']

        #ind = 1
        #while (len(self.pedidos.json()['retorno']['pedidos']) == 100):
        #    ind = ind + 1
        #    url = f"https://bling.com.br/Api/v2/pedidos/page={ind}/json/"
        #    payload = {"apikey": KeyApi}

        #    self.pedidos = requests.get(url, params=payload)
        #    All = All + self.pedidos.json()['retorno']['pedidos']

    def todos(self):
        return All

class produto(object):

    #All = NULL

    def __init__(self, sku):
        url = f"https://bling.com.br/Api/v2/produto/{sku}/json/"
        payload = {"apikey": KeyApi, "imagem": "S", "estoque": "S"}

        #https://bling.com.br/Api/v2/produto/{sku}/json?apikey=keyyy&imagem=S

        self.produtos = requests.get(url, params=payload)

        global All
        All = self.produtos.json()

        while str(All).replace("{", "").replace("}", "") == "'retorno': 'erros': 'erro': 'cod': 18, 'msg': 'O limite de requisições por segundo foi atingido, tente novamente mais tarde.'":
            self.produtos = requests.get(url, params=payload)
            All = self.produtos.json()

    def tudo(self):
        #print(str(All))
        return All

    def imagens(self):
        lista = []
        for im in All['retorno']['produtos'][0]['produto']['imagem']:
            lista.append(im['link'])
        return lista
    def sku(self):
        return All['retorno']['produtos'][0]['produto']['codigo']
    def titulo(self):
        return All['retorno']['produtos'][0]['produto']['descricao']
    def condicao(self):
        return All['retorno']['produtos'][0]['produto']['condicao']
    def marca(self):
        return All['retorno']['produtos'][0]['produto']['marca']
    def imagem(self, ind):
        return All['retorno']['produtos'][0]['produto']['imagem'][f'{ind}']['link']