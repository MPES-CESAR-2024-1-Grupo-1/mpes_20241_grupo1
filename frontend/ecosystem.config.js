/* eslint-disable prettier/prettier */
module.exports = {
    apps: [
        {
            name: 'fe_mpses',
            script: 'npm',
            args: 'start',
            // instances: 'max',
            // exec_mode: 'cluster',
            env: {
                NODE_ENV: 'production',
                PORT: 3000,
            },
        },
    ],
};
