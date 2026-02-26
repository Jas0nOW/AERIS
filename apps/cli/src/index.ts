import { AerisCore } from '@aeris/core';
import { AerisMemory } from '@aeris/memory';
import { Command } from 'commander';
import chalk from 'chalk';

const program = new Command();

program
  .name('aeris')
  .description('AERIS Supreme Orchestrator CLI')
  .version('0.1.0');

program.command('status')
  .description('Check the status of AERIS nodes')
  .action(() => {
    console.log(chalk.blue('AERIS CLI: ') + chalk.green('Online'));
    const core = new AerisCore();
    // In a real scenario, credentials would come from a secure vault
    const memory = new AerisMemory('https://your-supabase.url', 'your-key');
  });

program.parse();
