#!/bin/bash

python -m app.mcp.server &

streamlit run ui/streamlit_app.py \
  --server.port=7860 \
  --server.address=0.0.0.0