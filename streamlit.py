import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")  # Set the page layout to wide mode

def main():
  st.title("Excel Row Browser")

  # File uploader
  uploaded_file = st.file_uploader("Upload an Excel or csv file", type=["xlsx", "xls", "csv"])

  if uploaded_file is not None:
    df = pd.read_excel(uploaded_file)

    # 파일 이름에서 "T" 또는 "F" 포함 여부 확인
    file_name = uploaded_file.name.upper()  # 대소문자 구분 없이 처리
    if file_name == "E_QWEN2-5_1-5B.csv":
      target_personality = "Extravert (E)"
      comparison_prompt = f"""
      For clarity, here’s some background of this particular Energy Preferences dimension:
      Extravert (E) & Introversion (I) is about **Energy Preferences**: describes how people direct their mental energy and interact with their environment.
      
      Extravert (E) refers to drawing energy from the external world—through interaction, activity, and engagement with others. 
      They are energized by action and social environments. They are Expressive, Energetic, Sociable, Outgoing, and Active.  
      Extravert (E) Key characteristics: Outward energy and engagement with others.
      
      Introvert (I) on the contrary, refers to drawing energy from the internal world—through reflection, introspection, and by being alone. 
      They prefer calm, minimally stimulating environments.  
      Introvert (I) Key characteristics: Inward energy and being alone."""
    elif file_name == "I_QWEN2-5_1-5B.csv":
      target_personality = "Introvert (I)"
      comparison_prompt = f"""
      For clarity, here’s some background of this particular Energy Preferences dimension:
      Extravert (E) & Introversion (I) is about **Energy Preferences**: describes how people direct their mental energy and interact with their environment.
      
      Extravert (E) refers to drawing energy from the external world—through interaction, activity, and engagement with others. 
      They are energized by action and social environments. They are Expressive, Energetic, Sociable, Outgoing, and Active.  
      Extravert (E) Key characteristics: Outward energy and engagement with others.
      
      Introvert (I) on the contrary, refers to drawing energy from the internal world—through reflection, introspection, and by being alone. 
      They prefer calm, minimally stimulating environments.  
      Introvert (I) Key characteristics: Inward energy and being alone."""
    elif file_name == "N_QWEN2-5_1-5B.csv":
      target_personality = "Intuitive (N)"
      comparison_prompt = f"""
      For clarity, here’s some background of this particular Mind Preferences dimension:
      Intuitive (N) & Observant (S) is about **Mind Preferences**: describe how people prefer to gather and interpret information from the world.

      Intuitive (N) types focus on abstract ideas, theories, and future possibilities. 
      They are driven by imagination, patterns, and conceptual frameworks. 
      They often explore what could be, rather than what is, and seek meaning beneath the surface.  
      They are Imaginative, Conceptual, Abstract, Idealistic, and Insightful.  
      Intuitive (N) Key characteristics: Focus on patterns, concepts, and future-oriented possibilities.                       
      
      Observant (S) types focus on concrete facts, observable details, and present realities. 
      They are practical and grounded, relying on experience and sensory input. 
      They value realism and often prefer proven methods over speculation or abstract theory.  
      They are Practical, Realistic, Factual.  
      Observant (S) Key characteristics: Focus on facts, reality, and sensory information."""
    elif file_name == "S_QWEN2-5_1-5B.csv":
      target_personality = "Observant (S)"
      comparison_prompt = f"""
      For clarity, here’s some background of this particular Mind Preferences dimension:
      Intuitive (N) & Observant (S) is about **Mind Preferences**: describe how people prefer to gather and interpret information from the world.

      Intuitive (N) types focus on abstract ideas, theories, and future possibilities. 
      They are driven by imagination, patterns, and conceptual frameworks. 
      They often explore what could be, rather than what is, and seek meaning beneath the surface.  
      They are Imaginative, Conceptual, Abstract, Idealistic, and Insightful.  
      Intuitive (N) Key characteristics: Focus on patterns, concepts, and future-oriented possibilities.                       
      
      Observant (S) types focus on concrete facts, observable details, and present realities. 
      They are practical and grounded, relying on experience and sensory input. 
      They value realism and often prefer proven methods over speculation or abstract theory.  
      They are Practical, Realistic, Factual.  
      Observant (S) Key characteristics: Focus on facts, reality, and sensory information."""
    elif file_name == "F_QWEN2-5_1-5B.csv":
      target_personality = "Feeling (F)"
      comparison_prompt = f"""
      For clarity, here’s some background of this particular Decision-Making Preferences dimension:
      
      Thinking (T) & Feeling (F) is about **Decision-Making Preferences**: describes the way in which a person makes decisions and processes information.
      Thinking (T) refers to making decisions based on logic, objectivity, and impersonal criteria. 
      Thinkers prioritize truth, fairness, and consistency. They tend to be analytical, critical, and task-oriented. 
      Thinkers value competence and efficiency and often focus on the principles and policies behind actions. 
      They are Logical, Objective, Critical, Analytical, and Detached. 
      Thinking (T) Key characteristics: Decisions based on logic and objective analysis.
      
      Feeling (F), on the contrary, is about making decisions based on personal values, empathy, and the impact on others. 
      Feelers prioritize harmony, compassion, and relationships. 
      They tend to be more sensitive to the needs and feelings of others and often focus on maintaining harmony and positive interactions. 
      Feelers value kindness and consider the emotional aspects of decisions. They are Empathetic, Harmonious, Compassionate, Warm, and Subjective. 
      Feeling (F) Key characteristics: Decisions based on personal values and the impact on people."""
    elif file_name == "T_QWEN2-5_1-5B.csv":
      target_personality = "Thinking (T)"
      comparison_prompt = f"""
      For clarity, here’s some background of this particular Decision-Making Preferences dimension:
      Thinking (T) & Feeling (F) is about **Decision-Making Preferences**: describes the way in which a person makes decisions and processes information.
      
      Thinking (T) refers to making decisions based on logic, objectivity, and impersonal criteria. 
      Thinkers prioritize truth, fairness, and consistency. They tend to be analytical, critical, and task-oriented. 
      Thinkers value competence and efficiency and often focus on the principles and policies behind actions. 
      They are Logical, Objective, Critical, Analytical, and Detached. 
      Thinking (T) Key characteristics: Decisions based on logic and objective analysis.
      
      Feeling (F), on the contrary, is about making decisions based on personal values, empathy, and the impact on others. 
      Feelers prioritize harmony, compassion, and relationships. 
      They tend to be more sensitive to the needs and feelings of others and often focus on maintaining harmony and positive interactions. 
      Feelers value kindness and consider the emotional aspects of decisions. They are Empathetic, Harmonious, Compassionate, Warm, and Subjective. 
      Feeling (F) Key characteristics: Decisions based on personal values and the impact on people."""
    elif file_name == "J_QWEN2-5_1-5B.csv":
      target_personality = "Judging (J)"
      comparison_prompt = f"""
      For clarity, here’s some background of this particular Tactics Preferences dimension:
      Judging (J) & Prospecting (P) is about **Tactics Preferences**: describe how people deal with structure, planning, and flexibility in their lives.
      
      Judging (J) types prefer order, control, and decisiveness. 
      They seek closure and clarity, often making decisions early and sticking to plans. 
      They value predictability, routine, and having things settled and typically dislike last-minute changes. 
      They are Organized, Decisive, Structured.  
      Judging (J) Key characteristics: Preference for structure, order and plan.
      
      Prospecting (P) types prefer flexibility, spontaneity, and openness. 
      They enjoy keeping options open. They are more comfortable with uncertainty and change, and value exploration over closure. 
      They are Flexible, Spontaneous, and Open-ended.  
      Prospecting (P) Key characteristics: Preference for flexibility, openness."""
    elif file_name == "P_QWEN2-5_1-5B.csv":
      target_personality = "Prospecting (P)"
      comparison_prompt = f"""
      For clarity, here’s some background of this particular Tactics Preferences dimension:
      Judging (J) & Prospecting (P) is about **Tactics Preferences**: describe how people deal with structure, planning, and flexibility in their lives.
      
      Judging (J) types prefer order, control, and decisiveness. 
      They seek closure and clarity, often making decisions early and sticking to plans. 
      They value predictability, routine, and having things settled and typically dislike last-minute changes. 
      They are Organized, Decisive, Structured.  
      Judging (J) Key characteristics: Preference for structure, order and plan.
      
      Prospecting (P) types prefer flexibility, spontaneity, and openness. 
      They enjoy keeping options open. They are more comfortable with uncertainty and change, and value exploration over closure. 
      They are Flexible, Spontaneous, and Open-ended.  
      Prospecting (P) Key characteristics: Preference for flexibility, openness."""
    else:
      target_personality = "Thinking (T)"
      comparison_prompt = f"""
      For clarity, here’s some background of this particular Decision-Making Preferences dimension:
      Thinking (T) & Feeling (F) is about **Decision-Making Preferences**: describes the way in which a person makes decisions and processes information.
      
      Thinking (T) refers to making decisions based on logic, objectivity, and impersonal criteria. 
      Thinkers prioritize truth, fairness, and consistency. They tend to be analytical, critical, and task-oriented. 
      Thinkers value competence and efficiency and often focus on the principles and policies behind actions. 
      They are Logical, Objective, Critical, Analytical, and Detached. 
      Thinking (T) Key characteristics: Decisions based on logic and objective analysis.
      
      Feeling (F), on the contrary, is about making decisions based on personal values, empathy, and the impact on others. 
      Feelers prioritize harmony, compassion, and relationships. 
      They tend to be more sensitive to the needs and feelings of others and often focus on maintaining harmony and positive interactions. 
      Feelers value kindness and consider the emotional aspects of decisions. They are Empathetic, Harmonious, Compassionate, Warm, and Subjective. 
      Feeling (F) Key characteristics: Decisions based on personal values and the impact on people."""
      
    # Display the dataframe shape
    st.write(f"Total rows: {df.shape[0]}, Total columns: {df.shape[1]}")
      
    # Session state for row navigation
    if 'row_idx' not in st.session_state:
      st.session_state.row_idx = 0
      
    # Navigation buttons
    col1, col2, col3 = st.columns([1, 2, 1])
      
    with col1:
      if st.button("Previous"):
        st.session_state.row_idx = max(0, st.session_state.row_idx - 1)
      
    with col3:
      if st.button("Next"):
        st.session_state.row_idx = min(len(df) - 1, st.session_state.row_idx + 1)
      
    # Display selected row's index, first, and second columns with wider height
    row_idx = st.session_state.row_idx
    st.write(f"### Selected Row Index: {df.index[row_idx]}")

    st.markdown(
      f"""<div style='padding:10px; border:1px solid black; min-height:100px; width:100%;'>
      {comparison_prompt}</div>""", unsafe_allow_html=True
    )

    st.write(f"### **Target Personality: {target_personality}**")  # 선택된 성격 유형 표시

    st.markdown(
      f"""<div style='padding:10px; border:1px solid black; min-height:80px; width:100%;'>
      [Previous utterance] : {df.iloc[row_idx]['speaker_uttr']}</div>""", unsafe_allow_html=True
    )

    st.write(f"Compare the overall quality of these two responses and pick the one that is better at representing the Target Personality.")
      
    st.markdown(
      f"""**답변 1:**
      <div style='padding:10px; border:1px solid black; min-height:100px; width:100%;'>
      {df.iloc[row_idx]['base'] if row_idx % 2 == 0 else df.iloc[row_idx]['decisionMaking_generated_response_base']}</div>""", unsafe_allow_html=True
    )
      
    st.markdown(
      f"""**답변 2:**
      <div style='padding:10px; border:1px solid black; min-height:100px; width:100%;'>
       {df.iloc[row_idx]['decisionMaking_generated_response_base'] if row_idx % 2 == 0 else df.iloc[row_idx]['base']}</div>""", unsafe_allow_html=True
    )
  else:
    st.write("Please upload an Excel file to proceed.")

if __name__ == "__main__":
    main()
