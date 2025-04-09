from itertools import product

def is_endomorphism(f, M):
    """Vérifie si f préserve l'opération max"""
    for x, y in product(M, repeat=2):
        if f[max(x, y)] != max(f[x], f[y]):
            return False
    return True

def is_idempotent(f, M):
    """Vérifie si f ∘ f = f"""
    for x in M:
        if f[f[x]] != f[x]:
            return False
    return True

def generate_endomorphisms(n):
    """Génère tous les endomorphismes de M = {0,...,n} avec f(0) = 0"""
    M = list(range(n + 1))
    S = []
    for f_tuple in product(M, repeat=len(M)):
        f = {i: f_tuple[i] for i in M}
        if is_endomorphism(f, M) and f[0] == 0:
            S.append(f)
    return M, S

def right_annihilator(f, S, M):
    """Calcule r_S(f) = {g ∈ S | f∘g = 0}"""
    r = []
    zero = {x: 0 for x in M}
    for g in S:
        fog = {x: f[g[x]] for x in M}
        if fog == zero:
            r.append(g)
    return r

def image_set(f, S, M):
    """Calcule Im_S(f) = {f∘g | g ∈ S}"""
    images = set()
    for g in S:
        fog = tuple(f[g[x]] for x in M)
        images.add(fog)
    return images

def f_compose_S(f, S, M):
    """Calcule fS = {f∘g | g ∈ S}"""
    fS = set()
    for g in S:
        fog = tuple(f[g[x]] for x in M)
        fS.add(fog)
    return fS

def find_generator(f, S, M):
    """Trouve un générateur minimal pour Im_S(f)"""
    # Implémentation simplifiée - peut nécessiter des ajustements
    for g in S:
        if tuple(g.values()) in image_set(f, S, M):
            return g
    return f

def is_i_rickart(S, M):
    """Vérifie si S est i-Rickart"""
    for f in S:
        if is_idempotent(f, M):
            f_composed = {tuple(f[g[x]] for x in M) for g in S}
            if f_composed == {tuple(f[x] for x in M)}:
                return True
    return False

def subtractive_closure(S, M):
    """Calcule la clôture soustractive Im_S(f) pour tous les f ∈ S"""
    closure = set()
    for f in S:
        im = image_set(f, S, M)
        closure.update(im)
    return {tuple(f[x] for x in M) for f in S} == closure

def is_w_rickart(S, M):
    """Vérifie si S est w-Rickart"""
    if not is_i_rickart(S, M):
        return False
    return subtractive_closure(S, M)

def generate_latex_table(M, S):
    # Assigner des identifiants aux fonctions
    func_tuples = [tuple(f[i] for i in M) for f in S]
    sorted_funcs = sorted(func_tuples)
    func_ids = {t: f"f_{i}" for i, t in enumerate(sorted_funcs)}
    
    # Préparer les données du tableau
    table_data = []
    for i, f_tuple in enumerate(sorted_funcs):
        f = {x: f_tuple[x] for x in M}
        f_id = func_ids[f_tuple]
        
        # Calculer les propriétés
        r_s = right_annihilator(f, S, M)
        f_s = f_compose_S(f, S, M)
        im_s = image_set(f, S, M)
        generator = find_generator(f, S, M)
        
        # Formater pour LaTeX
        r_s_str = "\\{ " + ", ".join(func_ids[tuple(g[x] for x in M)] for g in r_s) + " \\}"
        f_s_str = "\\{ " + ", ".join(func_ids[t] for t in f_s) + " \\}"
        im_s_str = "\\{ " + ", ".join(func_ids[t] for t in im_s) + " \\}"
        gen_str = f"<{func_ids[tuple(generator[x] for x in M)]}>"
        
        table_data.append((f_id, f_tuple, r_s_str, f_s_str, im_s_str, gen_str))
    
    # Générer le tableau LaTeX
    latex_table = r"""\begin{table}[h]
\centering
\begin{tabular}{|c|c|c|c|c|}
\hline
\( f_i \) & \( r_{S}(f_i) \) & \( f_i S \) & \( \text{Im}_{S}(f_i) \) & \( \text{ generator } \)\\ 
\hline
"""
    
    for f_id, f_tuple, r_s, f_s, im_s, gen in table_data:
        latex_table += f"\( {f_id}= {f_tuple} \) & \( {r_s} \) & \( {f_s} \) & \( {im_s} \) & \( {gen} \) \\\\ \n"
    
    latex_table += r"""\hline
\end{tabular}
\caption{Table of the endomorphisms \( f_i \), their sets \( r_{S}(f_i) \), \( \text{Im}_{S}(f_i) \) and \( f_i S \).}
\end{table}"""
    
    return latex_table

def test_rickart_properties(n):
    M, S = generate_endomorphisms(n)
    print(f"Analyse pour M = {list(M)} (n={n}):")
    print(f"Nombre d'endomorphismes: {len(S)}")
    
    # Générer le tableau
    latex_table = generate_latex_table(M, S)
    print(latex_table)
    
    # Tester les propriétés de Rickart
    i_rickart = is_i_rickart(S, M)
    w_rickart = is_w_rickart(S, M) if i_rickart else False
    
    print("\nConclusion:")
    if i_rickart:
        print("S est i-Rickart.")
        if w_rickart:
            print("S est w-Rickart.")
        else:
            print("S n'est pas w-Rickart.")
    else:
        print("S n'est pas i-Rickart.")

# Exemple d'utilisation
n = 2  # Vous pouvez changer cette valeur
test_rickart_properties(n)