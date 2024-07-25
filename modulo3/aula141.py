class MyContextManager:
    def __init__(self, caminho_arquivo, modo):
        self.caminho_arquivo = caminho_arquivo
        self.modo = modo
        self._arquivo = None
    def __enter__(self):
        print('abrindo arquivo')
        self._arquivo = open(self.caminho_arquivo, self.modo,encoding='utf8')
        return self._arquivo

    def __exit__(self, class_exeception, exception_, traceback_):
        print('fechando arquivo')
        self._arquivo.close()

with MyContextManager('aula141.txt','w') as arquivo:
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')
    arquivo.write('Linha 3\n')
    print('with', arquivo)