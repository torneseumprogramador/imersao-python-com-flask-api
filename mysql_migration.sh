source env_vars.sh

for file in infraestrutura/db/mysql/migrations/*.sql; do
    if ! grep -Fxq "$file" infraestrutura/db/mysql/migrations/executados.txt; then
        mysql -u"$USER" -p"$PASS" < "$file"
        echo "$file" >> infraestrutura/db/mysql/migrations/executados.txt
    fi
done
