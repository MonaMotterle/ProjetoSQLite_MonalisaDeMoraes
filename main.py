from database import BancoDeDados

if __name__ == "__main__":
	
	banco = BancoDeDados()
	banco.conecta()
	banco.criar_tabelas()
	#banco.inserir_cliente('marcos', 'python', '11111111111', 'mcastrosouza@live.com')
	#banco.inserir_cliente('thomas', 'javascript', '22222222222', 'thomas@gmail.com')
	#print(banco.login('thomas', 'javascript'))
	#banco.buscar_email('thomas@gmail.com')
	#banco.buscar_cliente('11111111111')
	#banco.remover_cliente('22222222222')
	banco.desconecta()