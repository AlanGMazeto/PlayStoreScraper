mkdir -p ~/.streamlit/echo "\
[general]\n\
email = \"alan.geovani.mazeto@gmail.com\"\n\
" > ~/.streamlit/credentials.tomlecho "\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = 5000\n\
" > ~/.streamlit/config.toml