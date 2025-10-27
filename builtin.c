#include "headers/builtin.h"
#include "headers/utils.h"
#include "headers/history.h"
#include "headers/jobs.h"

// Built-in cd command
int builtin_cd(command_t *cmd) {
    char *dir = NULL;
    
    if (cmd->argc > 1) {
        dir = cmd->args[1];
    } else {
        // Default to home directory
        dir = getenv("HOME");
        if (!dir) {
            print_error("cd: HOME not set");
            return 1;
        }
    }
    
    // Expand tilde if present
    char *expanded_dir = expand_tilde(dir);
    if (!expanded_dir) {
        print_error("cd: Memory allocation failed");
        return 1;
    }
    
    if (chdir(expanded_dir) == -1) {
        print_error_with_errno("cd");
        free(expanded_dir);
        return 1;
    }
    
    free(expanded_dir);
    return 0;
}

// Built-in pwd command
int builtin_pwd(command_t *cmd) {
    (void)cmd;  // Suppress unused parameter warning
    char cwd[1024];
    if (getcwd(cwd, sizeof(cwd)) != NULL) {
        printf("%s\n", cwd);
        return 0;
    } else {
        print_error_with_errno("pwd");
        return 1;
    }
}

// Built-in echo command
int builtin_echo(command_t *cmd) {
    for (int i = 1; i < cmd->argc; i++) {
        printf("%s", cmd->args[i]);
        if (i < cmd->argc - 1) {
            printf(" ");
        }
    }
    printf("\n");
    return 0;
}

// Built-in exit command
int builtin_exit(command_t *cmd) {
    int exit_code = 0;
    
    if (cmd->argc > 1) {
        exit_code = atoi(cmd->args[1]);
    }
    
    // Clean up before exit
    cleanup_shell();
    exit(exit_code);
}

// Built-in history command
int builtin_history(command_t *cmd) {
    int count = MAX_HISTORY;
    
    if (cmd->argc > 1) {
        count = atoi(cmd->args[1]);
        if (count <= 0) {
            print_error("history: Invalid count");
            return 1;
        }
    }
    
    print_history(count);
    return 0;
}

// Built-in jobs command
int builtin_jobs(command_t *cmd) {
    (void)cmd;  // Suppress unused parameter warning
    print_jobs();
    return 0;
}

// Built-in fg command (foreground)
int builtin_fg(command_t *cmd) {
    if (cmd->argc < 2) {
        print_error("fg: job number required");
        return 1;
    }
    
    int job_id = atoi(cmd->args[1]);
    if (job_id <= 0) {
        print_error("fg: Invalid job number");
        return 1;
    }
    
    return resume_job(job_id, 1); // 1 for foreground
}

// Built-in bg command (background)
int builtin_bg(command_t *cmd) {
    if (cmd->argc < 2) {
        print_error("bg: job number required");
        return 1;
    }
    
    int job_id = atoi(cmd->args[1]);
    if (job_id <= 0) {
        print_error("bg: Invalid job number");
        return 1;
    }
    
    return resume_job(job_id, 0); // 0 for background
}
