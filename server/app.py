def main():
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=8000)


if _name_ == "_main_":
    main()
