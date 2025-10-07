from collections import defaultdict

class Solution:
    def minRunesToAdd(self, a, b, c, d):
        e = defaultdict(list)  # adjacency list from node to list of nodes
        f = defaultdict(list)  # reverse adjacency list (unused in this code)

        g = 0
        while g < len(a):
            h = a[g]
            i = b[g]
            e[h].append(i)
            f[i].append(h)
            g += 1

        indices = [-1] * d
        low_links = [0] * d
        on_stack = [False] * d
        stack = []
        index = 0
        sccs = []

        def tarjan(jj):
            nonlocal index
            kk = index
            indices[jj] = kk
            low_links[jj] = kk
            index += 1
            stack.append(jj)
            on_stack[jj] = True

            ll = 0
            neighbors = e.get(jj, [])
            while ll < len(neighbors):
                mm = neighbors[ll]
                if indices[mm] == -1:
                    tarjan(mm)
                    # low_links[jj] = min(low_links[jj], low_links[mm])
                    if low_links[jj] < low_links[mm]:
                        low_links[jj] = low_links[jj]
                    else:
                        low_links[jj] = low_links[mm]
                else:
                    if on_stack[mm]:
                        # low_links[jj] = min(low_links[jj], indices[mm])
                        if low_links[jj] < indices[mm]:
                            low_links[jj] = low_links[jj]
                        else:
                            low_links[jj] = indices[mm]
                ll += 1

            if low_links[jj] == indices[jj]:
                nn = False
                oo = []
                while not nn:
                    pp = stack.pop()
                    on_stack[pp] = False
                    oo.append(pp)
                    if pp == jj:
                        nn = True
                sccs.append(oo)

        uu = 0
        while uu < d:
            if indices[uu] == -1:
                tarjan(uu)
            uu += 1

        scc_graph = defaultdict(list)
        scc_index = [-1] * d
        scc_has_crystal = [False] * len(sccs)

        scc_count = 0
        xx = 0
        while xx < len(sccs):
            yy = 0
            while yy < len(sccs[xx]):
                node = sccs[xx][yy]
                scc_index[node] = scc_count

                found_crystal = False
                zz = 0
                while zz < len(c):
                    if c[zz] == node:
                        found_crystal = True
                        break
                    zz += 1
                if found_crystal:
                    scc_has_crystal[xx] = True

                yy += 1
            scc_count += 1
            xx += 1

        aa = 0
        while aa < len(c):
            bb = a[aa]
            cc_v = b[aa]
            u_scc = scc_index[bb]
            v_scc = scc_index[cc_v]
            if u_scc != v_scc:
                scc_graph[u_scc].append(v_scc)
            aa += 1

        in_degree = [0] * len(sccs)
        ee = 0
        while ee < len(sccs):
            ff = 0
            for ff in scc_graph.get(ee, []):
                in_degree[ff] += 1
            ee += 1

        additional_runes = 0
        hh = 0
        while hh < len(sccs):
            if in_degree[hh] == 0 and not scc_has_crystal[hh]:
                additional_runes += 1
            hh += 1

        return additional_runes