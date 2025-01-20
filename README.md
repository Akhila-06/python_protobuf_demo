**Step 1**

Create my_data.proto

```
syntax = "proto3";

message MyData {
  int32 id = 1;
  string name = 2;
  float value = 3;
}

```

**Step 2**

```
protoc --python_out=. my_data.proto
```

**Step 3**

```
poetry add protobuf
```

**Note:** Remember protoc --version should be same as protobuf pypi library

Create Python file process.py

**Step 4**

```
poetry run python process.py
```

This creates .bin file

