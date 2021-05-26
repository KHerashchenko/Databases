# connection credentials
# DB_URL = os.environ['DB_URL']
# DB_URL = "postgresql+psycopg2://test_user:password@127.0.0.1:5432/test_db"
DB_URL = "postgres://yomxuhokfcutki:78f28ae054911dd33268de28b33a6ad00cd23bc8eb9eafe435ed1163fea5ef3d@ec2-3-217-219-146.compute-1.amazonaws.com:5432/dam7srrq1v0ka9"

# entities properties
ACTOR_FIELDS = ['id', 'name', 'gender', 'date_of_birth']
MOVIE_FIELDS = ['id', 'name', 'year', 'genre', 'director_id']
DIRECTOR_FIELDS = ['id', 'name', 'gender', 'date_of_birth']

# date of birth format
DATE_FORMAT = '%Y-%m-%d'