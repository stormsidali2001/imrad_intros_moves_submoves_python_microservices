The directory contains the models data
```
moves 
    0 
        data
...

sub_moves_0
    0 
        data

sub_moves_1
    0 
        data

sub_moves_2
    0 
        data

```
And the models.config file

```

model_config_list: {
  config {
    name:  "moves",
    base_path:  "/models/moves",
    model_platform: "tensorflow"
  },
  config {
    name:  "sub_moves_0",
    base_path:  "/models/sub_moves_0",
    model_platform: "tensorflow"
  },
  config {
    name:  "sub_moves_1",
    base_path:  "/models/sub_moves_1",
    model_platform: "tensorflow"
  },
  config {
    name:  "sub_moves_2",
    base_path:  "/models/sub_moves_2",
    model_platform: "tensorflow"
  }
}
```