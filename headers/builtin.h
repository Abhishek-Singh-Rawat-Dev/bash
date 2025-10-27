#ifndef BUILTIN_H
#define BUILTIN_H

#include "shell.h"

// Function prototypes
int builtin_cd(command_t *cmd);
int builtin_pwd(command_t *cmd);
int builtin_echo(command_t *cmd);
int builtin_exit(command_t *cmd);
int builtin_history(command_t *cmd);
int builtin_jobs(command_t *cmd);
int builtin_fg(command_t *cmd);
int builtin_bg(command_t *cmd);

#endif
