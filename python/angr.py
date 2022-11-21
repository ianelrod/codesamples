import angr as a
import claripy as c
import logging as l

# You can avoid that by manually managing the stashes usually

# r = '/challenge/'
# e = os.getenv('CHALLENGE_NAME')
# b = context.binary = ELF(r + e)
# b = context.binary = ELF('./babyrev_level12.1')

flag_name = '/flag'
simfile = a.SimFile(flag_name, content='pwn.college\{practice\}\n')

main = \
    {
        'base_addr': 0
    }

load = \
    {
        'auto_load_libs': False
    }

# , support_selfmodifying_code=True
p = a.Project('./babyrev_level19.0', main_opts=main, load_options=load)
cfg = p.analyses.CFG(show_progressbar=True)

unicorn = \
    { 
        a.options.FAST_REGISTERS,
        # a.options.FAST_MEMORY,
        a.options.LAZY_SOLVES,
        a.options.UNICORN_SYM_REGS_SUPPORT,
        a.options.INITIALIZE_ZERO_REGISTERS,
        a.options.UNICORN
    }

stdin_chars = [c.BVS('flag_%d' % i, 8) for i in range(3)]
stdin = c.Concat(*stdin_chars)

# , add_options=unicorn, mode='tracing'
state = p.factory.entry_state(args=['./babyrev_level19.0'], stdin=stdin, fs={flag_name: simfile})
simgr = p.factory.simulation_manager(state)

# for b in stdin.chop(8):
#     state.add_constraints(b != 0)

# for i in stdin_chars:
#     state.solver.add()

l.getLogger('angr.sim_manager').setLevel('INFO')
simgr.use_technique(a.exploration_techniques.MemoryWatcher())
simgr.use_technique(a.exploration_techniques.Spiller())
simgr.use_technique(a.exploration_techniques.LoopSeer())
# simgr.use_technique(a.exploration_techniques.Veritesting())
# 
simgr.explore(find=lambda s: b"pwn.college" in s.posix.dumps(1), avoid=lambda s: b"INCORRECT!" in s.posix.dumps(1))

if(len(simgr.found)>0):
    for found in simgr.found:
        # print(simgr.found[0].fs.get(flag_name).concretize())
        print(simgr.found[0].solver.eval(stdin,cast_to=bytes))
else:
    print("No solution found")
