from models.connection.redis_conn import RedisConnectionHandle
from models.repository import RedisRepository

redis_conn = RedisConnectionHandle().connect()
redis_repo = RedisRepository(redis_conn)

redis_repo.insert("Estou", "Aqui!!!")
redis_repo.get('Estou')

redis_repo.insert_hash('my_hash','Nome','Weverton')
redis_repo.insert_hash('my_hash','Idade',18)
valor = redis_repo.get_hash('my_hash','Nome')
print(valor)