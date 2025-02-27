from os.path import join

from google_drive_downloader import GoogleDriveDownloader as gdd


models = {
    'alan-watts': '1TxMWBLuN-GLBMB3ebi5uIbq374jt6HE7',
    'bible': '1x8SQgqZyLGRdHRV6BUIHEPxZuWUCyhRc',
    'harry': '1-3iQhw89Biyv1QMf4o2BEahoPX9g3fNd',
    'meditations': '1-9TiibA0_dqD7dqyJnBNBrZnLuegAa_E',
    'tolkien': '1-0lq9cGClSqcvcI3WqGkxdmAdoWrhD4e',
    'asimov': '1yg4bORU_KpV4h_aVnbMaekulK6ShpCS1',
    'hemingway': '1-0p2I9SCL37JEaIlIGhasbvOc4lxQIq6'
}


def download_from_gdrive(
    name,
    drive_id,
    prefix,
    unzip,
    suffix='zip',
):
    print('downloading {}'.format(name))

    gdd.download_file_from_google_drive(
        file_id=drive_id,
        dest_path=join(
            prefix,
            f'{name}.{suffix}'
        ),
        unzip=unzip
    )


def download_models(models, prefix='./models', unzip=False):
    for name, drive_id in models.items():
        download_from_gdrive(
            name=name,
            drive_id=drive_id,
            prefix=prefix,
            unzip=unzip
        )


if __name__ == '__main__':
    download_models(models)
