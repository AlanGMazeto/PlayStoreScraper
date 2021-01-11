mkdir -p ~/.streamlit

echo "
[general]
email = \"alan.geovani.mazeto@gmail.com\"
" > ~/.streamlit/credentials.toml

echo "
[server]
headless = true
enableCORS=false
port = $PORT
" > ~/.streamlit/config.toml