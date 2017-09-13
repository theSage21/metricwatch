MetricWatch
===========

![Graphs appear here](graph.png)


Instructions for use
--------------------

To add a new project,

1. Fork this repository
2. All projects to be monitored must have `.performance_metrics` file in their root directory.
3. Run the commands
    ```bash
    git clone https://github.com/myOwnForkOf/metricwatch
    cd metricwatch
    git submodule add https://github.com/someUser/someProject
    git add -Av
    git commit -m 'added submodule someProject'
    ```
4. Update graphs with
    ```bash
    cd metricwatch
    make
    git add -Av
    git commit -m 'update'
    git push origin master
    ```

The `.performance_metrics` file follows the following format:

```
n concurrent users : 50
```

The first is the legend key, the second is the floating value. You can update this file over time and it's history will be tracked over time using git. Multiple projects have their own subplots. This plot is shown in this README file.

It is the repo's responsibility to maintain the `.performance_metrics` file and update it over time.
