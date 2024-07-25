# Abstração/ Eu nao quero que a pessoa use esse classe diretamante, colocando o erro de implementaçao
# log
from pathlib import Path

Log_file = Path(__file__).parent / 'log.txt'

class Log:
    def _log(self, msg):
        raise NotImplementedError('IMPLEMENTE O METEDO LOG')
    def log_error(self,msg):
        return self._log(f'Error:{msg}')
    def log_success(self,msg):
        return self._log(f'Success: {msg}')


# Herança - e um
class LogFileMixin(Log):
    def _log(self, msg):
        mgs_fortmatada = f'{msg}({self.__class__.__name__})'
        print('Salvando no log', mgs_fortmatada)
        with open(Log_file,'a') as arquivo:
            arquivo.write(mgs_fortmatada)
            arquivo.write('\r\n')
        print(msg)

class LogPrintMixin(Log):
    def _log(self,msg):
        print(f'{msg} ({self.__class__.__name__})')

if __name__ == '__main__':
    lp = LogPrintMixin()
    lp.log_error('qualquer coisa')
    lp.log_success('Que legal')
    lf = LogFileMixin()
    lf.log_error('qualquer coisa')
    lf.log_success('Que legal')
