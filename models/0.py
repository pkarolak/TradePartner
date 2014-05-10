from gluon.storage import Storage
settings = Storage()

settings.migrate = True
settings.title = 'TradePartner'
settings.subtitle = 'trade always with the best'
settings.author = 'Patryk Karolak'
settings.author_email = 'patryk.karolak@akai.org.pl'
settings.keywords = 'tradepartner, dostawcy, producenci, kontakt'
settings.description = 'TradePartner'
settings.layout_theme = 'Default'
settings.database_uri = 'sqlite://storage.sqlite'
settings.security_key = '393e0957-ed87-453f-a0dc-de0fe87cea24'
settings.login_method = 'local'
settings.login_config = ''
settings.plugins = []


