from invocate import task


@task(namespace='dev', name='run-server')
def run_dev_server(c):
    c.run(
        'npm run dev',
        pty=True,
    )


@task(namespace='dev', name='install-dependencies')
def install_dev_dependencies(c):
    c.run('npm install')
