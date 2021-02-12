# %% [markdown]
# # opdracht-1
# Sorteer een rij van n getallen op 2 manieren:
# ## Decrease and conquer
# ### inductiehypothese
#
# ### pseudocode
#
# p(n):
#   als rij 1 lang
#       dan geef terug rij
#   anders
#       sla hoogste getal op
#       haal hoogste getal uit lijst
#       geef terug p(n - 1) + grootste getal
#
# ### uitwerking


def p(n):
    if len(n) == 1:
        return n
    else:
        m = max(n)
        del n[n.index(m)]
        return p(n) + [m]

# %%[markdown]
# ## Devide and conquer
# ### inductiehypothese
#
# ### pseudocode
#
# ### uitwerking
#


def p(n):
    pass

# %% [markdown]
# # opdracht 2
# Draai een string van s letters om
# ### inductiehypothese
#
# ### pseudocode
#
# p(n):
#   als lengte woord 1
#       geef terug woord
#   anders:
#       geeft terug laatste letter + (woord tot laatste letter)
#
# ### uitwerking


def p(n):
    if len(n) == 1:
        return n
    else:
        return n[-1] + p(n[:-1])


p("test zin")

# %% [markdown]
# # opdracht 3
# Gegeven een weegschaal en (een lijst van) n stukken lood van verschillende
# gewichten. Verdeel de n gewichten zodanig dat de weegschaal (zoveel mogelijk)
# in balans is

# %% [markdown]
# # opdracht 4
# Het spel ‘De torens van Hanoi’ bestaat uit een stapel van N verschillende
# schijven en drie pinnen: de bron (S), de hulp (A) en de bestemming (D).

# %%
