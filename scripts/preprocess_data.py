import argparse
from multiprocessing import Pool

from igp2.data import ScenarioConfig

from ogrit.core.data_processing import prepare_episode_dataset


def main():
    parser = argparse.ArgumentParser(description='Process the dataset')
    parser.add_argument('--scenario', type=str, help='Name of scenario to process', default=None)
    parser.add_argument('--workers', type=int, help='Number of multiprocessing workers', default=2)
    parser.add_argument('--extract_indicator_features', help='If you want to extract the indicator features',
                        action='store_true')

    args = parser.parse_args()

    if args.scenario is None:
        scenarios = ['heckstrasse', 'bendplatz', 'frankenberg'] # , 'round']
    else:
        scenarios = [args.scenario]

    params_list = []
    for scenario_name in scenarios:
        scenario_config = ScenarioConfig.load(f"scenarios/configs/{scenario_name}.json")
        for episode_idx in range(len(scenario_config.episodes)):
            if args.extract_indicator_features:
                # We want to extract the indicator features on top of the base features.
                params_list.append((scenario_name, episode_idx, True))
            else:
                params_list.append((scenario_name, episode_idx))

    with Pool(args.workers) as p:
        p.map(prepare_episode_dataset, params_list)


if __name__ == '__main__':
    main()
