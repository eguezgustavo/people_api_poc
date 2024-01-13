import api

if __name__ == "__main__":
    app = api.create_api()
    app.run(host="0.0.0.0", port=8081, debug=True)
