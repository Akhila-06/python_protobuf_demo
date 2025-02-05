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

**Note:** Remember protoc --version should be same or closer as protobuf minor version number from pypi library.

In my setup protoc --version = 29.3, pypi protobuf = 5.29.2
Minor version of protobuf is 29.2 which is closer to 29.3


Create Python file my_data_process.py

**Step 4**

```
poetry run python my_data_process.py
```

This creates .bin file

