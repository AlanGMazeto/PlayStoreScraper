mkdir -p ~/.streamlit

echo "
[general]
email = \"alan.geovani.mazeto@gmail.com\"
" > ~/.streamlit/credentials.toml

echo "
[server]
headless = true
port = $PORT
enableCORS=false
" > ~/.streamlit/config.toml