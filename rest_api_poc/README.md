# Rest Api

### Install
```shell
pip install flask-restful
```

### Usage
```shell
python rest-api.py
```

* Hello World endpoint
```
curl -X GET http://localhost:5000
```

* List all tasks
```
curl -X GET http://localhost:5000/tasks
```

* Create a task
```
curl -X POST http://localhost:5000/tasks/{id}?taskName={value}
```

* Get unique task by id
```
curl -X GET http://localhost:5000/tasks/{id}
```
