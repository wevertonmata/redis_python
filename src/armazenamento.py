from datetime import datetime

from models.connection.redis_conn import RedisConnectionHandle
from models.repository import RedisRepository
from configs.start_form import start_form

##########################
# 1. Conectar ao banco de dados e buscar elemento
redis_conn = RedisConnectionHandle().connect()
redis_repo = RedisRepository(redis_conn)

data_atual = datetime.now()
data_form = data_atual.strftime('%Y-%m-%d')

# busca
hash_items = redis_conn.hgetall(f'Clientes_{data_form}')
print(hash_items)


#########################################
#2. Carregar dados ao dicionário
python_dict = {}
for key, value in hash_items.items():
    python_dict[key.decode('utf-8')] = value.decode('utf-8')
    
print(python_dict)
start_form.load_info(python_dict)

#########################################
# 3. Utilizar valor armazenado
value = start_form.get_info('Maicon')
value2 = start_form.get_info('Andre')
print(f"{value} e {value2}")

#########################################
