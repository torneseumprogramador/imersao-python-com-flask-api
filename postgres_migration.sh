source env_vars.sh

for file in infraestrutura/db/postgres/migrations/*.sql; do
    if ! grep -Fxq "$file" infraestrutura/db/postgres/migrations/executados.txt; then
        pg_restore --username="$USER" --password="$PASS" --host="$HOST" --port="5432" --dbname="$DATABASE" "$file"
        echo "$file" >> infraestrutura/db/postgres/migrations/executados.txt
    fi
done
