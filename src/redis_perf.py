from models.redis.connection.redis_conn import RedisConnectionHandle
from models.redis.repository import RedisRepository
from models.mysql.repository import MysqlRepository


redis_conn = RedisConnectionHandle().connect()
redis_repo = RedisRepository(redis_conn)
mysql_repo = MysqlRepository()

name = "Weverton"

print("Buscando info no Redis")
busca = redis_repo.get(name)

if busca:
    print("Achei no Redis!!!!")
    print(busca)
else:
    print("Buscando no MySql")
    valor = mysql_repo.select_by_name(name)
    if valor:
        print('Achei no MySQL!!!')
        redis_repo.insert_ex(name, valor, 10)
    else: 
        print("Not found")