# fuel-stations

Work in progress. The purpose of this app is to provide an easy to use interface for evaluating if its possible to travel between two different cities in an electric vehicle (EV). Range anxiety is a well known barrier to mass EV adoption, so something like this can be used to evaluate whether your favorite road trips are possible given your vehicles range and the current state of the EV charging network.

## Run the project locally

1. Clone the repo and cd into the fuel-stations folder.

2. Set up the back end python environment and dependencies

Move to the api sub-folder

```
cd vehicle_network_api
```

create the conda fuel-stations environment

```bash
conda env create -f environment.yml && conda activate fuel-stations
```

3. Set up the front end dependencies

```bash
npm install
```

4. Create the vehicle network files

```bash
npm run build-networks
```

5. Start the backend flask app

```bash
npm run start-api
```

6. Start the front end dev server

```bash
npm run dev
```

## Reference

Build containers

```bash
docker-compose build
```

Run containers

```bash
docker-compose up
```

Save conda environment

```bash
cd vehicle_network_api
conda env export --from-history > environment.yml
```

Get docker image size

```bash
docker images | grep fuel-stations
```

Current sizes
fuel-stations_frontend latest b3d2b2f1632a 24 seconds ago 2.26GB
fuel-stations_vehicle_network_api latest 025936fb260a 47 seconds ago 3.06GB
