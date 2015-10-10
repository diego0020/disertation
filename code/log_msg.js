// Syntax
{
type : "log",
action: <description of user action>,
state : <resulting state of the application>,
pid : <pid_of target application|id browser session>,
application :  <name of application>,
time : timestamp when the action happened,
sceensshot : <optional, not yet implemented, image_id?>
}

// Example
{
type: "log",
action: subject changed,
state : {current_subject: 10, variables: [45, 14,32], plot: ['scatter']},
pid : 1546,
application : 'anova',
time : 105130014
}

