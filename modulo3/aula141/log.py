# Abstração/ Eu nao quero que a pessoa use esse classe diretamante, colocando o erro de implementaçao
# log
class Log:
    def _log(self, msg):
        raise NotImplementedError('IMPLEMENTE O METEDO LOG')
    def log_error(self,msg):
        return self._log(f'Error:{msg}')
        


# Herança - e um
class LogFileMixin(Log):
    def _log(self, msg):
        print(msg)

class LogPrintMixin(Log):
    def _log(self,msg):
        print(f'{msg} ({self.__class__.__name__})')

if __name__ == '__main__':
    l = LogPrintMixin()
    l.log_error('TESTE')
