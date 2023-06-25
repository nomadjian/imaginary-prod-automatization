sed -i 's/DB_USER/'"$POSTGRES_USER"'/g' alembic.ini
sed -i 's/DB_PASS/'"$POSTGRES_PASSWORD"'/g' alembic.ini
sed -i 's/DB_NAME/'"$POSTGRES_DB"'/g' alembic.ini
sed -i 's/DB_PORT/'"$POSTGRES_PORT"'/g' alembic.ini
sed -i 's/DB_URL/'"$POSTGRES_URL"'/g' alembic.ini
exec "$@"