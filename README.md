# Locust Performance Tests

## Run in Master-Worker Mode

**Start master:**

```bash
locust -f simulations/demo_locustfile.py --master
```

**Start workers** (in separate terminals):

```bash
locust -f simulations/demo_locustfile.py --worker
locust -f simulations/demo_locustfile.py --worker
```

Access web UI at: <http://localhost:8089>
