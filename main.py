import numpy as np
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

st.set_page_config(page_title="Heitor Anderson", layout="wide")

st.markdown("""
<style>
/* Sidebar dark */
section[data-testid="stSidebar"]{
  background:#1E1E2F; padding:20px 16px;
}

/* Esconder a bolinha do radio (funciona em versões novas e antigas) */
div[role="radiogroup"] > label > div:first-child,
div[role="radiogroup"] input[type="radio"],
div[role="radiogroup"] div[role="radio"] > div:first-child{
  display:none !important;
}


/* Itens do menu: mesma largura (100%), mais longos e com fundo */
div[role="radiogroup"] > label,
div[role="radiogroup"] div[role="radio"]{
  display:flex; justify-content:center; align-items:center;
  width:100% !important; height:56px;
  margin:8px 0; padding:0 12px;
  border-radius:12px; background:#2C2C3E;
  color:#FFFFFF !important; font-weight:500;
  cursor:pointer; transition:all .25s ease;
  text-align:center;
}

/* Hover */
div[role="radiogroup"] > label:hover,
div[role="radiogroup"] div[role="radio"]:hover{
  background:#3E3E5E;
}

/* Selecionado (compatível com variações do Streamlit) */
div[role="radiogroup"] > label[data-checked="true"],
div[role="radiogroup"] div[role="radio"][aria-checked="true"]{
  background:#4B6EA9 !important; font-weight:700;
}
</style>
""", unsafe_allow_html=True)

st.sidebar.markdown("## Heitor Anderson")
st.sidebar.markdown("---")


menu = st.sidebar.radio(
    label="",
    options=["Quem sou eu", "Análise de Dados"],
    key="menu",
    label_visibility="collapsed"
)
st.sidebar.markdown("---")

if menu == "Quem sou eu":
    st.title("👤 Quem sou eu")

    st.write("""
    Olá! Meu nome é ***Heitor Anderson Prestes de Oliveira Filho***. 
    
    Sou estudante de tecnologia com interesse em cibersegurança e redes de computadores.
    
    Tenho experiência prática com Python, Linux e Packet Tracer, ferramentas que considero essenciais para construir uma base sólida em segurança da informação.
    Meu objetivo é atuar na área de cybersecurity, contribuindo para a proteção de sistemas e redes contra ameaças digitais.
    """)

    st.markdown("---")

    st.markdown("### 🎓 Formação")
    st.write("""
    - Bacharelado em Engenharia de Software — FIAP (2024 - 2027)
    """)

    st.markdown("---")

    st.markdown("### 💼 Experiência")
    st.write("""
    - Desenvolvimento de pequenos projetos e scripts em **Python**  
    - Configuração e uso de ambientes **Linux**  
    - Simulação de redes utilizando **Packet Tracer**  
    """)

    st.markdown("---")

    st.markdown("### 🛠️ Habilidades")
    st.write("**Python**: automação de tarefas, análise de dados e scripts práticos")
    st.write("**Linux**: administração básica, comandos essenciais e gerenciamento de sistemas")
    st.write("**Packet Tracer**: simulação de topologias de rede, configuração de roteadores e switches")

    st.markdown("---")

    st.markdown("### 📫 Contato")
    st.write("""
    - Email: heitorprestes59@gmail.com  
    - LinkedIn: https://linkedin.com/in/heitor-oliveira-05a9b12b6
    - GitHub: https://github.com/heitorprestes 
    """)

elif menu == "Análise de Dados":
    st.title("📊 Análise de Dados")


    try:
        df = pd.read_csv("Global_Cybersecurity_Threats_2015-2024.csv")

        st.subheader("📄 Visualização dos dados")
        st.dataframe(df, use_container_width=True)
        st.write("""
        O dataset **Global Cybersecurity Threats (2015-2024)** reúne informações sobre as principais ameaças de cibersegurança registradas ao longo de quase uma década.  
        Ele contém dados que permitem identificar **tendências, evolução temporal e distribuição de diferentes tipos de ataques** em nível global.  

        Entre os aspectos que podem ser analisados estão:  
        - Frequência e crescimento de incidentes ao longo dos anos.  
        - Tipos de ameaças mais comuns (malware, phishing, ransomware, etc.).  
        - Distribuição geográfica dos ataques e setores mais afetados.  
        - Indicadores estatísticos que ajudam a avaliar **impacto e gravidade** das ameaças.
        """)

        st.title("**Tipos de Variaveis**")

        st.markdown("""
        Country: Coluna que indica o nome do país e ela é do tipo Qualitativa Nominal

        Year: Coluna que indica o ano do ataque e ela é do tipo Quantitativa Discreta

        Attack Type: Coluna que indica o tipo ataque e ela é do tipo Quantitativa Nominal

        Target Industry: Coluna que indica o tipo da indústria atacada e ela é do tipo Quantitativa Nominal

        Financial Loss: Coluna que indica a perda financeira no ataque e ela é do tipo Quantitativa Contínua

        Number of Affected Users: Coluna que indica o número de usuário afetados pelo ataque e ela é do tipo Quantitativa Contínua

        Attack Source: Coluna que indica a fonte do ataque e ela é do tipo Qualitativa Nominal

        Security Vulnerabiity Type: Coluna que indica o tipo de vulnerabilidade e ela é do tipo Qualitativa Nominal

        Defense Mechanism Used: Coluna que indica o tipo de mecanismo de defesa usado para combater o ataque, e ela é do tipo Quantitativa Nominal

        Incident Resolution Time: Coluna que indica em quanto tempo o incidente foi solucionado(em horas) e ela é do tipo Quantitativa Discreta
        """)

        st.title("Distribuição de dados")

        st.markdown("""
        - **Distribuição temporal**: Os registros estão espalhados por uma década, permitindo observar **padrões de crescimento** nas ameaças e picos em determinados anos.  
        - **Distribuição geográfica**: A coluna *Country* mostra a presença de ataques em diversos países, o que possibilita analisar quais regiões concentram mais incidentes.  
        - **Tipos de ataque**: A variável *Attack Type* destaca técnicas recorrentes como **phishing, ransomware e man-in-the-middle**, algumas aparecendo com muito mais frequência que outras, o que evidencia a **predominância de certos vetores de ataque**.  
        - **Setores alvo**: A coluna *Target Industry* revela que determinados setores, como **educação, TI e telecomunicações**, aparecem repetidamente como alvos prioritários, sugerindo maior vulnerabilidade nessas áreas.  
         **Distribuição numérica**:  
        - *Financial Loss (in Million $)* mostra perdas variando de valores moderados até **impactos financeiros elevados**, indicando grande variabilidade entre os ataques.  
        - *Number of Affected Users* apresenta forte dispersão: alguns incidentes atingem poucos usuários, enquanto outros envolvem **centenas de milhares**, apontando para eventos de alto impacto.  
        - *Incident Resolution Time* também varia bastante, refletindo tanto respostas rápidas com uso de tecnologias avançadas quanto atrasos na mitigação.  

        Essa distribuição evidencia que as ameaças **não ocorrem de forma uniforme**: certos tipos de ataque, setores e países concentram a maior parte dos incidentes, enquanto outros aparecem de forma esporádica.  
        Isso reforça a importância de políticas de **defesa direcionadas** para as áreas mais críticas e vulneráveis.
        """)

        st.subheader("📈 Estatísticas descritivas")
        st.write(df.describe())
        st.subheader("🎯 Moda (valores mais frequentes)")
        colunas_numericas = df.select_dtypes(include="number").columns

        if len(colunas_numericas) > 0:
            resumo_numerico = pd.DataFrame({
                "Média": df[colunas_numericas].mean(),
                "Mediana": df[colunas_numericas].median(),
                "Moda": df[colunas_numericas].mode().iloc[0],
                "Desvio Padrão": df[colunas_numericas].std()
            })
            st.dataframe(resumo_numerico, use_container_width=True)
        else:
            st.warning("Nenhuma coluna numérica encontrada para calcular estatísticas.")

        st.markdown("""
        ***PERDAS FINANCEIRAS (FINANCIAL LOSS IN MILLION $):***


        A média das perdas financeiras mostra o impacto médio dos incidentes, mas a mediana está um pouco diferente, o  que pode sugerir a presença de ataques grandes que distorcem os resultados.

        A moda, próxima de 18 milhões de dólares, representa um valor recorrente de prejuízo típico em diversos casos.

        O desvio padrão elevado indica grande variabilidade entre os incidentes, mostrando que alguns ataques tiveram impacto financeiro muito maior que outros.

        ***USUÁRIOS AFETADOS (NUMBER OF AFFECTED USERS):***
        

        A média e a mediana se mantêm relativamente próximas, sugerindo uma distribuição menos distorcida, mesmo que  ainda existam incidentes de grande escala.

        A moda, em torno de 164 mil usuários, indica um patamar recorrente de impacto.

        O desvio padrão reforça que há casos isolados com milhões de usuários atingidos, elevando a dispersão dos dados.

        ***TEMPO DE RESOLUÇÃO(INCIDENT RESOLUTION TIME IN HOURS):***
        

        A média de resolução mostra que muitas organizações levam dezenas de horas para conter ataques.

        A mediana é ligeiramente menor, sinalizando que a maior parte dos incidentes é resolvida mais rapidamente, mas alguns casos demoram um pouco mais, o que fazem a média ser um pouco maior.

        A moda, em 43 horas, representa o tempo de resposta mais frequente.

        O desvio padrão mostra grande variação no tempo de resolução, o que pode refletir diferenças na preparação e nas habilidades das equipes de resposta a incidentes.
        """)

        st.subheader("🔠 Estatísticas categóricas")

        colunas_categoricas = df.select_dtypes(include="object").columns

        if len(colunas_categoricas) > 0:
            resumo_categorico = {}
            for col in colunas_categoricas:
                moda = df[col].mode().iloc[0] if not df[col].mode().empty else "N/A"
                freq = df[col].value_counts().iloc[0] if not df[col].value_counts().empty else 0
                resumo_categorico[col] = {"Valor mais frequente": moda, "Frequência": freq}

            resumo_categorico_df = pd.DataFrame(resumo_categorico).T
            st.dataframe(resumo_categorico_df, use_container_width=True)
        else:
            st.warning("Nenhuma coluna categórica encontrada.")

    except FileNotFoundError:
        st.error("❌ O arquivo 'Global_Cybersecurity_Threats_2015-2024.csv' não foi encontrado na pasta do projeto.")

        st.subheader("📊 Análise das Variáveis Categóricas")

    st.markdown("""
    A análise das variáveis categóricas revela os padrões mais recorrentes no conjunto de dados:
    
    - **Ano mais registrado:** 2017, indicando maior concentração de incidentes nesse período.  
    - **País mais afetado:** Reino Unido (UK), sugerindo forte incidência ou melhor registro local.  
    - **Tipo de ataque predominante:** DDoS, destacando-se como vetor mais utilizado.  
    - **Setor mais visado:** Tecnologia da Informação (IT), setor altamente exposto e crítico.  
    - **Fonte de ataque mais frequente:** Estados-nação (Nation-state), apontando para forte atividade de ameaças patrocinadas.  
    - **Vulnerabilidade mais explorada:** Zero-day, ressaltando a gravidade de falhas desconhecidas.  
    - **Defesa mais utilizada:** Antivírus, ainda comum apesar de suas limitações contra ataques modernos.  
    """)


    st.subheader("🔗 Análise de Correlação")


    df_num = df.select_dtypes(include="number")

    if df_num.shape[1] < 2:
        st.warning("Não há colunas numéricas suficientes para calcular a correlação.")
    else:
        corr = df_num.corr()

        fig, ax = plt.subplots(figsize=(8, 6))
        cax = ax.matshow(corr, cmap="coolwarm")
        fig.colorbar(cax)
        ax.set_xticks(range(len(corr.columns)))
        ax.set_yticks(range(len(corr.columns)))
        ax.set_xticklabels(corr.columns, rotation=45, ha="left")
        ax.set_yticklabels(corr.columns)
        st.pyplot(fig)

        st.markdown("""
        O mapa de calor acima mostra a correlação entre as variáveis numéricas do conjunto de dados.
        
        - As correlações estão **muito próximas de zero**, indicando ausência de relações lineares fortes.
        - **Perdas financeiras, usuários afetados e tempo de resolução** não apresentam uma ligação direta.
        - O impacto financeiro não depende necessariamente da quantidade de usuários atingidos.
        - O **tempo de resolução** também não se relaciona de forma clara com prejuízos ou número de vítimas.
        """)

        st.subheader("Intervalo de Confiança e Teste de Hipótese")

        # Selecionar a variável de interesse
        dados = df["Financial Loss (in Million $)"].dropna()

        media = np.mean(dados)
        desvio = np.std(dados, ddof=1)
        n = len(dados)

        alpha = 0.05
        t_critico = stats.t.ppf(1 - alpha/2, df=n-1)
        erro_padrao = desvio / np.sqrt(n)
        ic_inferior = media - t_critico * erro_padrao
        ic_superior = media + t_critico * erro_padrao

        teste = stats.ttest_1samp(dados, 10_000_000)
        p_valor = teste.pvalue / 2  # teste unilateral (maior que)
        resultado = "Rejeitamos H0 (média > 10M)" if (p_valor < alpha and media > 10_000_000) else "Não rejeitamos H0"

        fig1, ax1 = plt.subplots(figsize=(8,5))
        ax1.hist(dados, bins=30, color="skyblue", edgecolor="black")
        ax1.axvline(media, color="red", linestyle="--", label=f"Média = {media:,.0f}")
        ax1.set_title("Distribuição das Perdas Financeiras")
        ax1.set_xlabel("Perdas Financeiras (USD)")
        ax1.set_ylabel("Frequência")
        ax1.legend()
        st.pyplot(fig1)

        fig2, ax2 = plt.subplots(figsize=(6,4))
        ax2.errorbar(1, media, yerr=[[media-ic_inferior],[ic_superior-media]], fmt='o', color="blue", capsize=5)
        ax2.axhline(10_000_000, color="red", linestyle="--", label="Limite 10M")
        ax2.set_xlim(0,2)
        ax2.set_xticks([])
        ax2.set_ylabel("Perdas Financeiras (USD)")
        ax2.set_title("Média com Intervalo de Confiança 95%")
        ax2.legend()
        st.pyplot(fig2)

        st.subheader("""- Foi escolhido a coluna de perdas financeiras para analise pois é a variável de maior impacto para as organizações, diretamente relacionada ao prejuízo econômico. Entender sua média e variação é fundamental para avaliar riscos.""")

        st.markdown(f"""
        
        - Média estimada: **{media:,.2f} USD**
        - Intervalo de confiança 95%: **[{ic_inferior:,.2f} ; {ic_superior:,.2f}]**
        - Teste t (H₀: média ≤ 10M | H₁: média > 10M):  
          - valor-p = **{p_valor:.4f}**  
          - Conclusão: **{resultado}**
        
        **Intervalo de Confiança (IC):**
        Ao calcular o intervalo de confiança de 95% para a média das perdas financeiras, obtivemos uma estimativa que indica onde, com alto grau de confiança, se encontra o valor médio real das perdas registradas.Se novas amostras fossem coletadas repetidamente, em 95% delas a média real estaria dentro desse intervalo.Isto nos permite avaliar o grau de estabilidade e consistência do impacto financeiro ao longo dos anos analisados.
        
        **Teste de Hipótese:**
        Para complementar, foi conduzido um teste t de uma amostra com o objetivo de verificar se as perdas médias ultrapassam o patamar de 10 milhões de dólares.

        H₀ (hipótese nula): a média é menor ou igual a 10M.
        
        H₁ (hipótese alternativa): a média é maior que 10M.
        
        Os resultados do teste apresentaram um valor-p reduzido, o que nos leva a rejeitar a hipótese nula e aceitar que, com elevada evidência estatística, as perdas médias são de fato superiores a 10 milhões de dólares.""")
